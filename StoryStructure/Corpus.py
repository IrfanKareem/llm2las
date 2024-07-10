import random

from StoryStructure.Question import Question
from StoryStructure.Story import Story
from TranslationalModule.EventCalculus import eventCalculusAxioms


class Corpus:
    def __init__(self):
        self.constantModeBias = set()
        self.ECModeBias = set()
        self.nonECModeBias = set()
        self.stories = []
        self.backgroundKnowledge = eventCalculusAxioms()
        self.hypotheses = set()
        self.isEventCalculusNeeded = False
        self.choiceRulesPresent = False
        self.nonEventCalculusExamples = []
        self.eventCalculusExamples = []

    def append(self, story):
        self.stories.append(story)

    def addNonECExample(self, example):
        self.nonEventCalculusExamples.append(example)

    def addECExample(self, example):
        self.eventCalculusExamples.append(example)

    def reset(self):
        self.ECModeBias = set()
        self.hypotheses = set()
        self.isEventCalculusNeeded = False
        self.choiceRulesPresent = False
        self.nonEventCalculusExamples = []

    def __iter__(self):
        ''' Returns the Iterator object '''
        return CorpusIterator(self)

    def pop(self):
        return self.stories.pop()

    def updateConstantModeBias(self, newConstantModeBis):
        self.constantModeBias.update(newConstantModeBis)

    def setHypotheses(self, newHypotheses):
        self.hypotheses = newHypotheses

    def getHypotheses(self):
        return self.hypotheses

    def updateECModeBias(self, modeBias):
        self.ECModeBias.update(modeBias)

    def updateNonECModeBias(self, modeBias):
        self.nonECModeBias.update(modeBias)

    def addConstantModeBias(self, constantBias):
        self.constantModeBias.add(constantBias)

    def shuffle(self):
        random.seed(4)
        random.shuffle(self.stories)

    def getIndex(self, story: Story):
        return self.stories.index(story)

    def get(self, index):
        return self.stories[index]

    def __str__(self):
        sentenceRepresentation = ""
        for story in self.stories:
            sentenceRepresentation += str(story) + "\n\n"
        return sentenceRepresentation


class CorpusIterator:
    ''' Iterator class '''

    def __init__(self, corpus):
        self._corpus = corpus
        self._index = 0

    def __next__(self):
        if self._index < len(self._corpus.stories):
            result = self._corpus.stories[self._index]
            self._index += 1
            return result

        raise StopIteration


def pruneCorpus(corpus: Corpus, numExamples):
    newCorpus = Corpus()
    numQuestions = 0
    for story in corpus:
        currentStory = Story()
        newCorpus.append(currentStory)
        for sentence in story:
            currentStory.addSentence(sentence)
            if isinstance(sentence, Question):
                numQuestions += 1
            if numQuestions >= numExamples:
                return newCorpus
