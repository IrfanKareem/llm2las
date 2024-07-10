from StoryStructure.Question import Question
from StoryStructure.Sentence import Sentence
from StoryStructure.Story import Story
from TranslationalModule.BasicParser import BasicParser, getSubstitutedText
from TranslationalModule.EventCalculus import wrap


class DatasetParser(BasicParser):
    def __init__(self, trainCorpus, testCorpus, useSupervision=False, taskId=1):
        super().__init__(taskId)
        self.trainCorpus = trainCorpus
        self.testCorpus = testCorpus
        self.useSupervision = useSupervision


        for story in self.trainCorpus:
            for sentence in story:
                sentence.doc = self.nlp(self.coreferenceFinder(sentence, story))
        for story in self.testCorpus:
            for sentence in story:
                sentence.doc = self.nlp(self.coreferenceFinder(sentence, story))

        for story in self.trainCorpus:
            for sentence in story:
                if isinstance(sentence, Question):
                    self.parse(sentence)

        for story in self.testCorpus:
            for sentence in story:
                if isinstance(sentence, Question):
                    self.parse(sentence)

        for story in self.trainCorpus:
            for sentence in story:
                if not isinstance(sentence, Question):
                    self.parse(sentence)

        for story in self.testCorpus:
            for sentence in story:
                if not isinstance(sentence, Question):
                    self.parse(sentence)

        self.updateFluents()
        self.setEventCalculusRepresentation()

    def coreferenceFinder(self, statement: Sentence, story: Story):
        pronoun, possibilities = super().coreferenceFinder(statement, story)
        if not pronoun or not possibilities:
            return statement.text
        return getSubstitutedText(pronoun, possibilities[0], statement)

    def setEventCalculusRepresentation(self):
        for story in self.trainCorpus:
            for sentence in story:
                wrap(sentence)
        for story in self.testCorpus:
            for sentence in story:
                wrap(sentence)

    def updateFluents(self):
        for story in self.trainCorpus:
            for sentence in story:
                self.updateSentence(sentence)
        for story in self.testCorpus:
            for sentence in story:
                self.updateSentence(sentence)
