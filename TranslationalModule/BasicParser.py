import re
import spacy
from StoryStructure import Story
from StoryStructure.Corpus import Corpus
from StoryStructure.Question import Question
from StoryStructure.Sentence import Sentence
from TranslationalModule.ConceptNetIntegration import ConceptNetIntegration
from Utilities.ILASPSyntax import varWrapping, constWrapping, createConstantTerm
import requests
import json

LLM_SERVICE_URL = "http://YOUR_IP_ADDRESS:YOUR_PORT/logic/generate/"

def createPronounRegularExpression(pronoun):
    return re.compile("(^| )" + pronoun + "( |[.!?]$)")


def createNameRegularExpression(name):
    return "\\1" + name + "\\2"


def getSubstitutedText(pronoun, substitution, statement):
    pronounRegularExpression = createPronounRegularExpression(pronoun)
    nameRegularExpression = createNameRegularExpression(substitution)
    return re.sub(pronounRegularExpression, nameRegularExpression, statement.text)

def hasDativeParent(token):
    return token.head.dep_ == "dative"


class BasicParser:
    def __init__(self, taskId):
        self.nlp = spacy.load("en_core_web_lg")
        self.synonymDictionary = {}
        self.conceptNet = ConceptNetIntegration()
        self.conceptsToExplore = set()
        self.determiningConcepts = {}
        self.temporalConstants = {}
        self.taskId = taskId

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
        response = requests.post(LLM_SERVICE_URL, data=json.dumps({'sentence': sentence, 'taskId': self.taskId}), headers={"Content-Type":'application/json'})
        
        if response.status_code == 200:
            parsed_data = response.json()
            
            fluent_representation = parsed_data.get("semantic_parse", "")
            
            if fluent_representation is not None:
                matches = [[x.group()] for x in re.finditer("[a-zA-z_]*\([a-zA-z]+([,a-zA-z0-9\s]+)?\)", fluent_representation.strip())]
                return matches
            else:
                return None
        else:
            print("Error in LLM server response")
            return None

            
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
            
            mode_bias_fluents = self.modebias(predicate, statement)
            statement.setModeBiasFluents(mode_bias_fluents)
        
        else:
            # Setting a default fluent representation if parsing fails
            statement.setFluents([[""]])
            statement.setModeBiasFluents([[""]])  # Set default modeBiasFluents

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