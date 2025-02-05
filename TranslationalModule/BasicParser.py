import re
import spacy
from StoryStructure import Story
from StoryStructure.Corpus import Corpus
from StoryStructure.Question import Question
from StoryStructure.Sentence import Sentence
from TranslationalModule.ConceptNetIntegration import ConceptNetIntegration
from Utilities.ILASPSyntax import varWrapping, constWrapping, createConstantTerm
import requests
from TranslationalModule.LLMCache import SemanticParsingCache
import json
from pathlib import Path 
import logging

LLM_SERVICE_URL = "http://127.0.0.1:8000/logic/generate/"
LLM_SERVICE_URL_MB = "http://127.0.0.1:8000/logic/generate_mb/"

def createPronounRegularExpression(pronoun):
    return re.compile("(^| )" + pronoun + "( |[.!?]$)")


def createNameRegularExpression(name):
    return "\\1" + name + "\\2"

def hasWHDeterminerChild(token):
    for child in token.children:
        if child.tag_ == "WDT":
            return True
    return False


def getSubstitutedText(pronoun, substitution, statement):
    pronounRegularExpression = createPronounRegularExpression(pronoun)
    nameRegularExpression = createNameRegularExpression(substitution)
    return re.sub(pronounRegularExpression, nameRegularExpression, statement.text)

def hasDativeParent(token):
    return token.head.dep_ == "dative"


class BasicParser:
    def __init__(self, taskId):
        self.nlp = spacy.load("en_core_web_sm")
        self.synonymDictionary = {}
        self.conceptNet = ConceptNetIntegration()
        self.conceptsToExplore = set()
        self.determiningConcepts = {}
        self.determiners = set()
        self.temporalConstants = {}
        self.taskId = taskId

        cache_folder = Path(".semantic-parsing-cache")
        cache_folder.mkdir(parents=True, exist_ok=True)
        self.cache = SemanticParsingCache((cache_folder / str(taskId)).as_posix())
        self.cache_mb = SemanticParsingCache((cache_folder / f'{str(taskId)}_mb' ).as_posix())

    def coreferenceFinder(self, statement: Sentence, story: Story):
        index = story.getIndex(statement)
        sentenceDoc = self.nlp(statement.text)
        personalPronoun = [token for token in sentenceDoc if token.tag_ == "PRP"]
        if index == 0 or not personalPronoun:
            return None, []
        possibleReferences = []
        for i in range(0, index):
            currentSentenceDoc = self.nlp(story.get(index - i - 1).text)
            properNoun = [token for token in currentSentenceDoc if token.pos_ == "PROPN"]
            if properNoun:
                replacementPhrase = properNoun[0].text
                if properNoun[0].conjuncts:
                    for noun in properNoun[0].conjuncts:
                        replacementPhrase += " and " + noun.text
                if replacementPhrase not in possibleReferences:
                    possibleReferences.append(replacementPhrase)
        return personalPronoun[0].text, possibleReferences
    

    def parse_llm(self, sentence: str):
        cache_hit = self.cache.get_cache(sentence)
        if cache_hit is None:
            response = requests.post(LLM_SERVICE_URL, data=json.dumps({'sentence': sentence, 'taskId': self.taskId}), headers={"Content-Type":'application/json'})
            if response.status_code != 200:
                raise RuntimeError("Error in LLM server response")
            
            response = response.json()
            print(f"[cache debug] Cache miss on {sentence}: got {response}, saving to cache")
            self.cache.write_cache(sentence, response)
        else:
            response = cache_hit 
            print(f"[cache debug] Cache hit on {sentence}: retrieved {response}")

        parsed_data = response          
        fluent_representation = parsed_data["semantic_parse"]
        print("Parsed: " + sentence + " Fluent: " + fluent_representation)
        
        if fluent_representation is not None:
            if '|' in fluent_representation:
                matches = [x.group() for x in re.finditer("[a-zA-z_]*\([a-zA-z]+([,a-zA-z0-9\s]+)?\)", fluent_representation.strip())]
                return [matches]
            else:
                matches = [[x.group()] for x in re.finditer("[a-zA-z_]*\([a-zA-z]+([,a-zA-z0-9\s]+)?\)", fluent_representation.strip())]
                return matches
        else:
            return None
        
    def parse_llm_mb(self, statement):
        
        to_parse = ''
        if len(statement.getFluents()[0])>1:##//Disjunzione
            to_parse = " | ".join(statement.getFluents()[0])
        else:
            to_parse = ", ".join([x[0] for x in statement.getFluents()])
        
        cache_hit = self.cache_mb.get_cache(statement.text+to_parse)
        if cache_hit is None:
            response = requests.post(LLM_SERVICE_URL_MB, data=json.dumps({'sentence': statement.text, 'fluent': to_parse}), headers={"Content-Type":'application/json'})
            if response.status_code != 200:
                raise RuntimeError("Error in LLM server response")
            
            response = response.json()
            print(f"[cache mb debug] Cache miss on {statement.text}: got {response}, saving to cache")
            #self.cache_mb.write_cache(statement.text+to_parse, response)
        else:
           response = cache_hit 
           print(f"[cache mb debug] Cache hit on {statement.text}: retrieved {response}")

        parsed_data = response          
        mbias_representation = parsed_data["semantic_parse"]
        print("Parsed: " + statement.text + " Mode bias: " + mbias_representation)
        
        mode_bias_fluents = None
        if mbias_representation is not None:
            aux_mb = re.sub(r"\s+", "", mbias_representation)
            if '|' in mbias_representation:
                #matches = [x.group() for x in re.finditer("[a-zA-z_]*\([a-zA-z]+([,a-zA-z0-9\s]+)?\)", mbias_representation.strip())]
                #return [matches]                
                self._add_constant_if_needed(statement, to_parse, aux_mb)
                #return [[x.strip() for x in aux_mb.strip().split("|")]]
                #return [mbias_representation.split("|")]
                mode_bias_fluents = [[x.strip() for x in aux_mb.strip().split("|")]]
            else:
                self._add_constant_if_needed(statement, to_parse, aux_mb)
                #matches = [[x.group()] for x in re.finditer("\w+\((?:var\([a-z]+\)|const\([a-z]+\))(?:,(?:var\([a-z]+\)|const\([a-z]+\)))*\)", aux_mb.strip())]
                #return matches
                mode_bias_fluents = [[x.group()] for x in re.finditer("\w+\((?:var\([a-z]+\)|const\([a-z]+\))(?:,(?:var\([a-z]+\)|const\([a-z]+\)))*\)", aux_mb.strip())]
            #return [[mbias_representation]]
            
            if cache_hit is None:
                if not isinstance(statement, Question) and len(self.determiners)>0:
                    self._adjust_mb_determiners(statement.getFluents(), mode_bias_fluents)           
            
                to_cache = ''
                if len(mode_bias_fluents[0])>1:##//Disjunzione
                    to_cache = " | ".join(statement.getFluents()[0])
                else:
                    to_cache = ", ".join([x[0] for x in mode_bias_fluents])                   
                    self.cache_mb.write_cache(statement.text+to_parse, {"sentence": statement.text, "semantic_parse": to_cache})
            
            return mode_bias_fluents
            
        else:
            return None
        
    def _adjust_mb_determiners(self, fluents, mb_fluents):
        for concept in self.determiners:
            for id, pred in enumerate(fluents):
                fluent_arguments = []
                for x in re.finditer(r"\(([^)]+)\)", pred[0].strip()):
                    fluent_arguments = fluent_arguments + x.group().replace("(", "").replace(")", "").split(",")                                                     
                for idx, arg in enumerate(fluent_arguments):
                    if self.conceptNet.isA(arg, concept, True):
                        re_mb_args = r"(var\([a-z]+\)|const\([a-z]+\))"
                        re_name = r'^\w+'
                        mb_args =  re.findall(re_mb_args, mb_fluents[id][0])
                        pred_name =  re.findall(re_name, mb_fluents[id][0])[0]
                        pred_name += "("
                        for i, mbarg in enumerate(mb_args):
                            if i == idx:
                                pred_name += f"var({concept})"
                            else:
                                pred_name = pred_name + f"{mbarg}," if i != len(mb_args)-1 else pred_name + f"{mbarg}"
                        pred_name += ")"
                        mb_fluents[id][0] = pred_name        
        
    def _add_constant_if_needed(self, statement, fluent, mb_fluent):
        '''
        Add constant mode bias to the statement if the fluent has a constant argument
        The function searches for the constant (const(type)) argument in the mode bias fluent:
            - If exists, the function searches for the argument in the fluent and adds it (addConstantModeBias).
        '''
        if "const(" in mb_fluent:
            re_mb_args = r"(var\([a-z]+\)|const\([a-z]+\))"
            re_fluent_args = r"\(([^)]+)\)"
            
            fluent_arguments = []
            for x in re.finditer(re_fluent_args, fluent.strip()):
                fluent_arguments = fluent_arguments + x.group().replace("(", "").replace(")", "").split(",")                
                
            for id, arg in enumerate(re.finditer(re_mb_args, mb_fluent)):
                if "const(" in arg.group(0) and id < len(fluent_arguments):
                    arg_type = arg.group(0).replace("const(", "").replace(")", "")
                    statement.addConstantModeBias(createConstantTerm(arg_type, fluent_arguments[id]))
        
            
    def modebias(self, fluents, statement):
        doc = self.nlp(statement.doc.text)
 
        # Check if the sentence is a "why" question
        is_why_question = statement.text.lower().startswith("why")
        if isinstance(statement, Question) and is_why_question:
            for answer in  statement.answer:
                statement.addConstantModeBias(createConstantTerm("jj", answer))
            

        is_what_color_question = statement.text.lower().startswith("what color")

        # Check if the sentence is a "where" question
        is_where_question = statement.text.lower().startswith("where")
        has_will = "will" in statement.text.lower()

        # Create a dictionary to store the words and their POS tags in lowercase
        pos_tags = {token.text.lower(): token.tag_.lower() for token in doc}        
        real_pos_tags = {token.text.lower(): token for token in doc} | {token.lemma_.lower(): token for token in doc}                         
        lemmas_pos_tags = {token.lemma_.lower(): token.tag_.lower()  for token in doc}
    
        pos_tags = pos_tags | lemmas_pos_tags
 
        # List of color words
        color_words = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'black', 'white', 'gray', 'brown']
 
        # Function to replace words with POS tags or const
        def replace(match):
            word = match.group(0).lower()
            if word == 'box_of_chocolates':
                return varWrapping('nn')
            if word in pos_tags:
                # if word in color_words:
                if pos_tags[word] == 'jj':
                    if word in color_words or is_what_color_question:
                        return varWrapping('color')
                    else:
                        if isinstance(statement, Question) and is_why_question:
                            statement.addConstantModeBias(createConstantTerm("jj", word))
                        return constWrapping("jj")
                        
                if self.isConstant(real_pos_tags[word]):
                    wrapping = constWrapping(pos_tags[word])
                    statement.addConstantModeBias(createConstantTerm(pos_tags[word], word))
                    return wrapping

                # If the word is a noun, use 'var(nn)' or 'var(nnp)' based on its POS tag
                elif pos_tags[word] in ['nn', 'nns']:
                    statement.addConstantModeBias(createConstantTerm("nn", word))
                    return varWrapping('nn')
                elif pos_tags[word] in ['nnp', 'nnps']:
                    return varWrapping('nnp')
                else:
                    # For other POS tags, use 'var' with the POS tag
                    return f"var({pos_tags[word]})"
            # Special condition for placeholders in questions, case-insensitive
            elif re.match(r'v\d+', word, re.IGNORECASE):
                if is_what_color_question:
                    return varWrapping('color')
                elif is_why_question:
                        wrapper = constWrapping("jj")
                        return wrapper
                elif is_where_question: 
                    if has_will:
                        return constWrapping("nn")
                    else:
                        return varWrapping('nn')
                # Use 'var(nnp)' for placeholders if the sentence starts with 'who'
                elif statement.text.lower().startswith("who"):
                    return varWrapping('nnp')
                else:
                    # Default to 'var(nn)' for other placeholders
                    return varWrapping('nn')
            return word
        # Function to replace words inside parentheses
        def replace_inside_parentheses(match):
            return re.sub(r'\b\w+\b', replace, match.group(0))
 
        ModeBiasFluents = []
        for fluent_list in fluents:
            mode_bias_fluent_list = []
            for fluent in fluent_list:
                # Replace words in the fluent with their POS tags
                new_fluent = re.sub(r'\([^)]+\)', replace_inside_parentheses, fluent)
                mode_bias_fluent_list.append(new_fluent)
            ModeBiasFluents.append(mode_bias_fluent_list)
        return ModeBiasFluents
    
    def parse(self, statement: Sentence):

        #Determining if there is negation in the sentence
        negation = [token for token in statement.doc if token.dep_ == 'neg' and token.tag_ == 'RB']
        if negation:
            statement.negatedVerb = True
        
        sentence_text = statement.doc.text
        predicate = self.parse_llm(sentence_text)

        if predicate:
            statement.setFluents(predicate) 

            possibleArguments = [token for token in statement.doc if "NN" in token.tag_ or (
                "JJ" in token.tag_ and "NN" not in token.head.tag_) or "W" in token.tag_]
            possibleArguments = self.orderNouns(possibleArguments, statement)
            
            #/////////////////////NEW//////////////////////////
            # to_parse = ''
            # if len(predicate[0])>1:##//Disjunzione
            #     to_parse = " | ".join(predicate[0])
            # else:
            #     to_parse = ", ".join([x[0] for x in predicate])
                
            #mode_bias = self.parse_llm_mb(sentence_text, predicate[0][0])
            mode_bias = self.parse_llm_mb(statement)
            
            #/////////////////////replacing with determiners//////////////////////////           
            if isinstance(statement, Question) and not statement.isYesNoMaybeQuestion():
                typeDeterminer = [token.lemma_ for token in statement.doc if hasWHDeterminerChild(token)]
                if typeDeterminer:
                    self.determiners.add(typeDeterminer[0])
            elif not isinstance(statement, Question) and len(self.determiners)>0:#There is a determiner to analyze
                for concept in self.determiners:
                    for id, pred in enumerate(predicate):
                        fluent_arguments = []
                        for x in re.finditer(r"\(([^)]+)\)", pred[0].strip()):
                            fluent_arguments = fluent_arguments + x.group().replace("(", "").replace(")", "").split(",")                                                     
                        for idx, arg in enumerate(fluent_arguments):
                            if self.conceptNet.isA(arg, concept, False):
                                re_mb_args = r"(var\([a-z]+\)|const\([a-z]+\))"
                                re_name = r'^\w+'
                                mb_args =  re.findall(re_mb_args, mode_bias[id][0])
                                pred_name =  re.findall(re_name, mode_bias[id][0])[0]
                                pred_name += "("
                                for i, mbarg in enumerate(mb_args):
                                    if i == idx:
                                        pred_name += f"var({concept})"
                                    else:
                                        pred_name = pred_name + f"{mbarg}," if i != len(mb_args)-1 else pred_name + f"{mbarg}"
                                pred_name += ")"
                                mode_bias[id][0] = pred_name
            if mode_bias:         
                #mode_bias_fluents = self.modebias(predicate, statement)
                #statement.setModeBiasFluents(mode_bias_fluents)
                statement.setModeBiasFluents(mode_bias)
                
                mb = re.sub(r"\s+", "", mode_bias[0][0])   
                prior_mb = self.modebias(predicate, statement)
                prior = prior_mb[0][0]
                prior = re.sub(r"\s+", "", prior)               
                logging.info(f"Sentence: {statement.text} MODE BIAS Fluent: {mb} PREDICATE: {prior_mb}")
                if(prior != mb):
                    logging.info(f"MODE BIAS Fluent ERRORR {str(prior == mb)}")        
              #  create here for determinaing color with isA
        
        else:
            # Setting a default fluent representation if parsing fails
            statement.setFluents([[""]])
            statement.setModeBiasFluents([[""]])  # Set default modeBiasFluents
            
    def createDeterminingConceptsEntry(self, entry, fluentBase):
        if entry in self.determiningConcepts.keys():
            return
        self.determiningConcepts[entry] = {}
        self.determiningConcepts[entry] = fluentBase

    def updateSentence(self, sentence: Sentence):
        fluents, modeBiasFluents = sentence.getFluents(), sentence.getModeBiasFluents()
        sentence.setFluents(self.updateFluentAndMBFluent(fluents))
        sentence.setModeBiasFluents(self.updateFluentAndMBFluent(modeBiasFluents))

    def updateFluentAndMBFluent(self, fluents):
        newFluents = []
        for i in range(0, len(fluents)):
            currentFluents = []
            for j in range(0, len(fluents[i])):
                predicate = fluents[i][j].split('(')[0]
                if predicate in self.synonymDictionary.keys():
                    updatedFluent = self.synonymDictionary[predicate]
                else:
                    updatedFluent = predicate
                updatedFluent = fluents[i][j].replace(predicate + '(', updatedFluent + '(')
                currentFluents.append(updatedFluent)
            newFluents.append(currentFluents)
        return newFluents
     
    def isConstant(self, noun):
        nounText = noun.text.lower()
        if nounText in self.temporalConstants.keys():
            return self.temporalConstants[nounText]
        for concept in self.determiningConcepts:
            if noun.text in self.determiningConcepts[concept]["inclusions"]:
                return False
        if noun.tag_.lower() == "jj":
            return True
        self.temporalConstants[nounText] = self.conceptNet.hasTemporalAspect(nounText)
        return self.temporalConstants[nounText]

    def orderNouns(self, nouns, statement: Sentence):
        sortedNouns = []
        nounSubject = [token for token in statement.doc if token.dep_ == "nsubj"]
        if nounSubject:
            sortedNouns.append(nounSubject[-1])
            directObject = [token for token in statement.doc if token.dep_ == "dobj"]
            if directObject:
                sortedNouns.append(directObject[0])

            indirectObject = [token for token in statement.doc if token.dep_ == "pobj" and hasDativeParent(token)]
            if indirectObject:
                sortedNouns.append(indirectObject[0])

        constants = [noun for noun in nouns if self.isConstant(noun) and noun not in sortedNouns]

        questionWords = [noun for noun in nouns if "W" in noun.tag_ and noun not in sortedNouns]

        for noun in nouns:
            if noun not in sortedNouns and noun not in constants and noun not in questionWords:
                sortedNouns.append(noun)
        for noun in constants:
            sortedNouns.append(noun)
        for noun in questionWords:
            sortedNouns.append(noun)
        return sortedNouns