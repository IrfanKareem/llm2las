import os
from LearningModule.heuristicGenerator import HeuristicGenerator
from StoryStructure.Question import Question
from StoryStructure.Sentence import Sentence
from StoryStructure.Story import Story
from TranslationalModule.ExpressivityChecker import createChoiceRule
from Utilities.ILASPSyntax import createTimeRange, maxVariables


def isSatisfiable(hypotheses):
    unsatisfiable = set()
    unsatisfiable.add("UNSATISFIABLE")
    return unsatisfiable != hypotheses


class Learner:
    def __init__(self, corpus, learningFile='/tmp/learningFile.las', cachingFile="/tmp/cachingFile.las",
                 useSupervision=False):
        self.filename = learningFile
        self.filename = os.path.expanduser("~/learningFile.las")
        self.cachingFile = cachingFile
        self.corpus = corpus
        self.useSupervision = useSupervision
        self.eventCalculusNeededPreviously = False
        self.currentExamplesIndex = 0
        self.heuristics = HeuristicGenerator(self.corpus)

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
            self.corpus.setHypotheses(hypotheses)

        self.eventCalculusNeededPreviously = self.corpus.isEventCalculusNeeded

    def __del__(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        if os.path.exists(self.cachingFile):
            os.remove(self.cachingFile)

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
        if self.corpus.isEventCalculusNeeded:
            for rule in self.corpus.backgroundKnowledge:
                file.write(rule)
                file.write('\n')
            for bias in self.corpus.ECModeBias:
                file.write(bias)
                file.write('\n')
        else:
            for bias in self.corpus.nonECModeBias:
                file.write(bias)
                file.write('\n')

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
        maxLiterals = self.heuristics.maxNumberOfLiterals()
        command = "ILASP -q -nc -ml=" + str(maxLiterals) \
                  + " --version=4 --cache-path=" + self.cachingFile + " " + self.filename
        output = os.popen(command).read()
        return self.processILASP(output)
        

    def processILASP(self, output):
        lines = output.split('\n')
        return set([line for line in lines if line])

    def addExamples(self, NonECExample, ECExample):
        self.corpus.addNonECExample(NonECExample)
        self.corpus.addECExample(ECExample)
