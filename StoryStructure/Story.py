from StoryStructure import Sentence


class Story:
    def __init__(self):
        self.sentences = []

    def __len__(self):
        return len(self.sentences)

    def addSentence(self, sentence):
        self.sentences.append(sentence)

    def getSentences(self):
        return self.sentences

    def getIndex(self, sentence: Sentence):
        return self.sentences.index(sentence)

    def get(self, index):
        return self.sentences[index]

    def __iter__(self):
        return StoryIterator(self)

    def __str__(self):
        sentenceRepresentation = ""
        for sentence in self.sentences:
            sentenceRepresentation += str(sentence) + " "
        return sentenceRepresentation


class StoryIterator:
    ''' Iterator class '''

    def __init__(self, story):
        self._story = story
        self._index = 0

    def __next__(self):
        if self._index < len(self._story.sentences):
            result = self._story.sentences[self._index]
            self._index += 1
            return result
        raise StopIteration
