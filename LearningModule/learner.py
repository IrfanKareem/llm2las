import os
from LearningModule.heuristicGenerator import HeuristicGenerator
from StoryStructure.Question import Question
from StoryStructure.Sentence import Sentence
from StoryStructure.Story import Story
from TranslationalModule.ExpressivityChecker import createChoiceRule
from Utilities.ILASPSyntax import createTimeRange, maxVariables
from pathlib import Path 

def check_file_not_empty(file):
    contents = Path(file).open('r').read()
    if len(contents.strip()) == 0:
        raise RuntimeError("Unexpected empty file:", file)


def isSatisfiable(hypotheses):
    is_unsatisfiable = "UNSATISFIABLE" in hypotheses
    return not is_unsatisfiable
    #unsatisfiable = set()
    #unsatisfiable.add("UNSATISFIABLE")
    #return unsatisfiable != hypotheses


class Learner:
    def __init__(self, corpus, learningFile='/tmp/learningFile.las', cachingFile="/tmp/cachingFile.las",
                 useSupervision=False, ilasp_version='4'):
        self.filename = learningFile
        self.filename = os.path.expanduser("~/learningFile.las")
        self.cachingFile = cachingFile
        self.corpus = corpus
        self.useSupervision = useSupervision
        self.eventCalculusNeededPreviously = False
        self.currentExamplesIndex = 0
        self.heuristics = HeuristicGenerator(self.corpus)
        self.ilasp_version = ilasp_version
        self.used_cache_files = []

    def learn(self, question: Question, story: Story, answer, createNewLearningFile=False):
        if self.corpus.choiceRulesPresent:
            if "maybe" in question.getAnswer():
                self.createPositiveExample(question, story, answer)
            else:
                self.createNegativeExample(question, story, answer)
        else:
            self.createPositiveExample(question, story, answer)

        if self.eventCalculusNeededPreviously != self.corpus.isEventCalculusNeeded or not os.path.exists(
                self.filename) or createNewLearningFile:
            if os.path.exists(self.cachingFile):
                os.remove(self.cachingFile)
            self.createLearningFile()
        else:
            self.appendExamplesToLearningFile()

        hypotheses = self.solveILASPTask()

        if isSatisfiable(hypotheses):
            print("LEARNED hypotheses: " + str(hypotheses))
            self.corpus.setHypotheses(hypotheses)

        self.eventCalculusNeededPreviously = self.corpus.isEventCalculusNeeded

    def __del__(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        if os.path.exists(self.cachingFile):
            os.remove(self.cachingFile)

        for cache_file in self.used_cache_files:
            if os.path.exists(cache_file):
                os.remove(cache_file)

    def createPositiveExample(self, question: Question, story: Story, answer):
        if "maybe" in question.getAnswer() or "yes" in question.getAnswer():
            self.createPositiveInclusion(question, story)
        elif "no" in question.getAnswer():
            self.createPositiveExclusion(question, story, answer)
        elif answer == ["nothing"] or answer == []:
            self.createPositiveInclusion(question, story)
        else:
            self.createPositiveExclusion(question, story, answer)

    def createNegativeExample(self, question: Question, story: Story, answer):
        if "yes" in question.getAnswer():
            self.createNegativeExclusion(question, story)
        elif "no" in question.getAnswer():
            self.createNegativeInclusion(question, story, answer)
        elif answer == ["nothing"]:
            self.createNegativeExclusion(question, story)
        else:
            self.createNegativeInclusion(question, story, answer)

    def createPositiveInclusion(self, question: Question, story: Story):
        positiveNonECPortion, positiveECPortion = question.createPartialInterpretation(question.getAnswer())
        nonECContext, ECContext = self.createContext(question, story)
        positiveNonECExample = '#pos(' + positiveNonECPortion + ',{},' + nonECContext + ').'
        positiveECExample = '#pos(' + positiveECPortion + ',{},' + ECContext + ').'
        self.addExamples(positiveNonECExample, positiveECExample)

    def createNegativeExclusion(self, question: Question, story: Story):
        positiveNonECPortion, positiveECPortion = question.createPartialInterpretation(question.getAnswer())
        nonECContext, ECContext = self.createContext(question, story)
        positiveNonECExample = '#neg(' + '{},' + positiveNonECPortion + "," + nonECContext + ').'
        positiveECExample = '#neg(' + '{},' + positiveECPortion + "," + ECContext + ').'
        self.addExamples(positiveNonECExample, positiveECExample)

    def createPositiveExclusion(self, question: Question, story: Story, answers):
        positiveNonECPortion, positiveECPortion = '{}', '{}'
        negativeNonECPortion, negativeECPortion = '{}', '{}'
        for answer in answers:
            if question.isCorrectAnswer([answer]):
                positiveNonECPortion, positiveECPortion = question.createPartialInterpretation([answer])
            else:
                negativeNonECPortion, negativeECPortion = question.createPartialInterpretation([answer])
        nonECContext, ECContext = self.createContext(question, story)
        negativeNonECExample = '#pos(' + positiveNonECPortion + ',' + negativeNonECPortion + ',' + nonECContext + ').'
        negativeECExample = '#pos(' + positiveECPortion + ',' + negativeECPortion + ',' + ECContext + ').'
        self.addExamples(negativeNonECExample, negativeECExample)

    def createNegativeInclusion(self, question: Question, story: Story, answer):
        negativeNonECPortion, negativeECPortion = question.createPartialInterpretation(answer)
        nonECContext, ECContext = self.createContext(question, story)
        negativeNonECExample = '#neg(' + negativeNonECPortion + ',{},' + nonECContext + ').'
        negativeECExample = '#neg(' + negativeECPortion + ',{},' + ECContext + ').'
        self.addExamples(negativeNonECExample, negativeECExample)

    def createContext(self, question: Question, story: Story):
        nonECContext, ECContext = '{', '{'
        if self.useSupervision:
            for hint in question.getHints():
                statement = story.get(int(hint) - 1)
                nonECContext, ECContext = self.addRepresentation(statement, nonECContext, ECContext)
        else:
            for statement in story:
                if not isinstance(statement, Question):
                    nonECContext, ECContext = self.addRepresentation(statement, nonECContext, ECContext)
                if statement == question:
                    break
        if nonECContext[-1] != '{':
            nonECContext += '.\n'
            ECContext += '.\n' + createTimeRange(question.getLineID()) + '.\n'

        nonECContext += '}\n'
        ECContext += '}\n'
        return nonECContext, ECContext

    def addRepresentation(self, statement: Sentence, nonECContext, ECContext):
        ECRepresentation = statement.getEventCalculusRepresentation()
        nonECRepresentation = statement.getFluents()
        for i in range(0, len(ECRepresentation)):
            ECRule = createChoiceRule(ECRepresentation[i], statement, eventCalculusUsage=True)
            nonECRule = createChoiceRule(nonECRepresentation[i], statement, eventCalculusUsage=False)
            if nonECContext[-1] != '{' and nonECContext[-1] != '\n':
                nonECContext += '.\n'
                ECContext += '.\n'
            nonECContext += nonECRule
            ECContext += ECRule
        return nonECContext, ECContext

    def createLearningFile(self):
        file = open(self.filename, 'w')
        hasConst = False
        if self.corpus.isEventCalculusNeeded:
            for rule in self.corpus.backgroundKnowledge:
                file.write(rule)
                file.write('\n')
            for bias in self.corpus.ECModeBias:
                print("BIAS: ", bias)
                if "#const(" in bias:
                    hasConst = True
                file.write(bias)
                file.write('\n')

        else:
            for bias in self.corpus.nonECModeBias:
                file.write(bias)
                file.write('\n')

        if hasConst:
            for constantBias in self.corpus.constantModeBias:
                file.write(constantBias)
                file.write('\n')

        file.write(maxVariables(self.heuristics.maximumNumberOfVariables()))

        file.write("#max_penalty(50).\n")

        if self.corpus.isEventCalculusNeeded:
            for example in self.corpus.eventCalculusExamples:
                file.write(example)
                file.write('\n')
        else:
            for example in self.corpus.nonEventCalculusExamples:
                file.write(example)
                file.write('\n')
        self.currentExamplesIndex = len(self.corpus.nonEventCalculusExamples)

        with open(self.filename, 'r') as file: 
            content = file.read() 
            print("LAS FILE -------")
            print(content)

    def appendExamplesToLearningFile(self):
        file = open(self.filename, 'a')
        for index in range(self.currentExamplesIndex, len(self.corpus.nonEventCalculusExamples)):
            if self.corpus.isEventCalculusNeeded:
                file.write(self.corpus.eventCalculusExamples[index])
            else:
                file.write(self.corpus.nonEventCalculusExamples[index])
            file.write('\n')
        self.currentExamplesIndex = len(self.corpus.nonEventCalculusExamples)
        file.close()

    def solveILASPTask(self):
        literals_ub = self.heuristics.maxNumberOfLiterals()
        
        for ml in range(2, literals_ub+1):
        #for ml in range(1, literals_ub+1):
            # TODO: Check with Mark if it is safe to re-use caching file across different number of MLs?
            cache_file = f"{self.cachingFile}_{ml}"
            self.used_cache_files.append(cache_file)
            command = f"ILASP -q -nc -ml={ml} --version={self.ilasp_version} --cache-path={cache_file} {self.filename}"
            print(f"Attempting to solve with #literals={ml}")
            print("Calling ILASP: ", command)
            from datetime import datetime
            print("STARTED AT: ", datetime.now().strftime("%H:%M:%S"))
            output = os.popen(command).read()
            ans = self.processILASP(output)
            print("FINISHED AT: ", datetime.now().strftime("%H:%M:%S"))
            if isSatisfiable(ans):
                return ans

        return {"UNSATISFIABLE"}
        

    def processILASP(self, output):
        lines = output.split('\n')
        return set([line for line in lines if line])

    def addExamples(self, NonECExample, ECExample):
        self.corpus.addNonECExample(NonECExample)
        self.corpus.addECExample(ECExample)


class LearnerV2:
    def __init__(self, 
                 corpus,
                 language_bias=Path('~/bias.las').expanduser(),
                 examples=Path('~/examples.las').expanduser(),
                 background_knowledge=Path('~/background.las').expanduser(),
                 cache=Path('~/cache.las').expanduser(),
                 useSupervision=False, 
                 ilasp_version='4'
    ):
        self.corpus = corpus
        self.language_bias_file = language_bias
        self.examples_file = examples
        self.background_knowledge_file = background_knowledge
        self.caching = cache
        self.useSupervision = useSupervision
        self.eventCalculusNeededPreviously = False
        self.currentExamplesIndex = 0
        self.heuristics = HeuristicGenerator(self.corpus)
        self.ilasp_version = ilasp_version
        self.used_cache_files = []

    def learn(self, question: Question, story: Story, answer, createNewLearningFile=False):
        if self.corpus.choiceRulesPresent:
            if "maybe" in question.getAnswer():
                self.createPositiveExample(question, story, answer)
            else:
                self.createNegativeExample(question, story, answer)
        else:
            self.createPositiveExample(question, story, answer)

        if self.eventCalculusNeededPreviously != self.corpus.isEventCalculusNeeded or not os.path.exists(
                self.background_knowledge_file) or createNewLearningFile:
            if os.path.exists(self.caching):
                os.remove(self.caching)
            self.createLearningFile()
        else:
            self.appendExamplesToLearningFile()

        hypotheses = self.solveILASPTask()

        if isSatisfiable(hypotheses):
            print("LEARNED hypotheses: " + str(hypotheses))
            self.corpus.setHypotheses(hypotheses)

        self.eventCalculusNeededPreviously = self.corpus.isEventCalculusNeeded

    def __del__(self):
        return 
    
        if os.path.exists(self.background_knowledge_file):
            os.remove(self.background_knowledge_file)
        if os.path.exists(self.examples_file):
            os.remove(self.examples_file)
        if os.path.exists(self.language_bias_file):
            os.remove(self.language_bias_file)
        if os.path.exists(self.caching):
            os.remove(self.caching)

        for cache_file in self.used_cache_files:
            if os.path.exists(cache_file):
                os.remove(cache_file)

    def createPositiveExample(self, question: Question, story: Story, answer):
        if "maybe" in question.getAnswer() or "yes" in question.getAnswer():
            self.createPositiveInclusion(question, story)
        elif "no" in question.getAnswer():
            self.createPositiveExclusion(question, story, answer)
        elif answer == ["nothing"] or answer == []:
            self.createPositiveInclusion(question, story)
        else:
            self.createPositiveExclusion(question, story, answer)

    def createNegativeExample(self, question: Question, story: Story, answer):
        if "yes" in question.getAnswer():
            self.createNegativeExclusion(question, story)
        elif "no" in question.getAnswer():
            self.createNegativeInclusion(question, story, answer)
        elif answer == ["nothing"]:
            self.createNegativeExclusion(question, story)
        else:
            self.createNegativeInclusion(question, story, answer)

    def createPositiveInclusion(self, question: Question, story: Story):
        positiveNonECPortion, positiveECPortion = question.createPartialInterpretation(question.getAnswer())
        nonECContext, ECContext = self.createContext(question, story)
        positiveNonECExample = '#pos(' + positiveNonECPortion + ',{},' + nonECContext + ').'
        positiveECExample = '#pos(' + positiveECPortion + ',{},' + ECContext + ').'
        self.addExamples(positiveNonECExample, positiveECExample)

    def createNegativeExclusion(self, question: Question, story: Story):
        positiveNonECPortion, positiveECPortion = question.createPartialInterpretation(question.getAnswer())
        nonECContext, ECContext = self.createContext(question, story)
        positiveNonECExample = '#neg(' + '{},' + positiveNonECPortion + "," + nonECContext + ').'
        positiveECExample = '#neg(' + '{},' + positiveECPortion + "," + ECContext + ').'
        self.addExamples(positiveNonECExample, positiveECExample)

    def createPositiveExclusion(self, question: Question, story: Story, answers):
        positiveNonECPortion, positiveECPortion = '{}', '{}'
        negativeNonECPortion, negativeECPortion = '{}', '{}'
        for answer in answers:
            if question.isCorrectAnswer([answer]):
                positiveNonECPortion, positiveECPortion = question.createPartialInterpretation([answer])
            else:
                negativeNonECPortion, negativeECPortion = question.createPartialInterpretation([answer])
        nonECContext, ECContext = self.createContext(question, story)
        negativeNonECExample = '#pos(' + positiveNonECPortion + ',' + negativeNonECPortion + ',' + nonECContext + ').'
        negativeECExample = '#pos(' + positiveECPortion + ',' + negativeECPortion + ',' + ECContext + ').'
        self.addExamples(negativeNonECExample, negativeECExample)

    def createNegativeInclusion(self, question: Question, story: Story, answer):
        negativeNonECPortion, negativeECPortion = question.createPartialInterpretation(answer)
        nonECContext, ECContext = self.createContext(question, story)
        negativeNonECExample = '#neg(' + negativeNonECPortion + ',{},' + nonECContext + ').'
        negativeECExample = '#neg(' + negativeECPortion + ',{},' + ECContext + ').'
        self.addExamples(negativeNonECExample, negativeECExample)

    def createContext(self, question: Question, story: Story):
        nonECContext, ECContext = '{', '{'
        if self.useSupervision:
            for hint in question.getHints():
                statement = story.get(int(hint) - 1)
                nonECContext, ECContext = self.addRepresentation(statement, nonECContext, ECContext)
        else:
            for statement in story:
                if not isinstance(statement, Question):
                    nonECContext, ECContext = self.addRepresentation(statement, nonECContext, ECContext)
                if statement == question:
                    break
        if nonECContext[-1] != '{':
            nonECContext += '.\n'
            ECContext += '.\n' + createTimeRange(question.getLineID()) + '.\n'

        nonECContext += '}\n'
        ECContext += '}\n'
        return nonECContext, ECContext

    def addRepresentation(self, statement: Sentence, nonECContext, ECContext):
        ECRepresentation = statement.getEventCalculusRepresentation()
        nonECRepresentation = statement.getFluents()
        for i in range(0, len(ECRepresentation)):
            ECRule = createChoiceRule(ECRepresentation[i], statement, eventCalculusUsage=True)
            nonECRule = createChoiceRule(nonECRepresentation[i], statement, eventCalculusUsage=False)
            if nonECContext[-1] != '{' and nonECContext[-1] != '\n':
                nonECContext += '.\n'
                ECContext += '.\n'
            nonECContext += nonECRule
            ECContext += ECRule
        return nonECContext, ECContext

    def createLearningFile(self):
        hasConst = False
        with open(self.language_bias_file, 'w') as lang_bias, open(self.examples_file, 'w') as examples, open(self.background_knowledge_file, 'w') as background_knowledge:
            if self.corpus.isEventCalculusNeeded:
                for rule in self.corpus.backgroundKnowledge:
                    background_knowledge.write(rule)
                    background_knowledge.write('\n')
                for bias in self.corpus.ECModeBias:
                    if "const(" in bias:
                        hasConst = True
                    lang_bias.write(bias)
                    lang_bias.write('\n')

            else:
                for bias in self.corpus.nonECModeBias:
                    if "const(" in bias:
                        hasConst = True
                    lang_bias.write(bias)
                    lang_bias.write('\n')

            if hasConst:
                for constantBias in self.corpus.constantModeBias:
                    lang_bias.write(constantBias)
                    lang_bias.write('\n')

            lang_bias.write(maxVariables(self.heuristics.maximumNumberOfVariables()))

            lang_bias.write("#max_penalty(50).\n")

            if self.corpus.isEventCalculusNeeded:
                for example in self.corpus.eventCalculusExamples:
                    examples.write(example)
                    examples.write('\n')
            else:
                for example in self.corpus.nonEventCalculusExamples:
                    examples.write(example)
                    examples.write('\n')
            self.currentExamplesIndex = len(self.corpus.nonEventCalculusExamples)


    def appendExamplesToLearningFile(self):
        with open(self.examples_file, 'a') as examples:
            for index in range(self.currentExamplesIndex, len(self.corpus.nonEventCalculusExamples)):
                if self.corpus.isEventCalculusNeeded:
                    examples.write(self.corpus.eventCalculusExamples[index])
                else:
                    examples.write(self.corpus.nonEventCalculusExamples[index])
                examples.write('\n')
            self.currentExamplesIndex = len(self.corpus.nonEventCalculusExamples)

    def solveILASPTask(self):
        literals_ub = self.heuristics.maxNumberOfLiterals()
        
        for ml in range(1, literals_ub+1):
            # Check if language bias already exists with the current number of literals
            if not Path(f"{self.language_bias_file}-{ml}").exists():
                
                print(f"Creating (ground) LAS bias file... @ {self.language_bias_file}-{ml}")
                command = f"ILASP -s -q -nc -ml={ml} --version={self.ilasp_version} {self.language_bias_file} > {self.language_bias_file}-{ml}"
                os.popen(command).read()


            else:
                print(f"{self.language_bias_file}-{ml} already exists. Skipping creation of bias file.")
                check_file_not_empty(f"{self.language_bias_file}-{ml}")

            cache_file = f"{self.caching}_{ml}"
            self.used_cache_files.append(cache_file)
            command = f"ILASP -q -nc -ml={ml} --version={self.ilasp_version} {self.background_knowledge_file} {self.examples_file} {self.language_bias_file}-{ml}"
            print(f"Attempting to solve with #literals={ml}")
            print("Calling ILASP: ", command)
            from datetime import datetime
            print("STARTED AT: ", datetime.now().strftime("%H:%M:%S"))
            output = os.popen(command).read()
            print("ILASP OUTPUT:")
            print(output)
            ans = self.processILASP(output)
            print("FINISHED AT: ", datetime.now().strftime("%H:%M:%S"))
            if isSatisfiable(ans):
                return ans

        return {"UNSATISFIABLE"}
        

    def processILASP(self, output):
        lines = output.split('\n')
        return set([line for line in lines if line])

    def addExamples(self, NonECExample, ECExample):
        self.corpus.addNonECExample(NonECExample)
        self.corpus.addECExample(ECExample)
