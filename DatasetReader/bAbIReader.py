from StoryStructure.Corpus import Corpus
from StoryStructure.Sentence import Sentence
from StoryStructure.Question import Question
from StoryStructure.Story import Story


def bAbIReader(filename):
    corpus = Corpus()
    file = open(filename, 'r')
    lines = file.readlines()
    story = Story()
    corpus.append(story)
    firstStory = True
    for line in lines:
        currentStatement = createStatement(line)
        if currentStatement.getLineID() == 1:
            if firstStory:
                firstStory = False
            else:
                newStory = Story()
                corpus.append(newStory)
        currentStory = corpus.pop()
        currentStory.addSentence(currentStatement)
        corpus.append(currentStory)
    return corpus


def createStatement(line):
    index = line.index(" ") + 1
    identification = line[:index - 1]
    data = line[index:].split("\t")
    text = data[0].strip()
    if len(data) == 1:
        return Sentence(identification, text)
    else:
        hints = data[2].strip('\n').split(" ")
        answer = data[1].split(',')
        return Question(identification, text, answer, hints)
