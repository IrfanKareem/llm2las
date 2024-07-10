import os
from StoryStructure.Corpus import Corpus
from StoryStructure.Question import Question
from StoryStructure.Story import Story
from TranslationalModule.ConceptNetIntegration import ConceptNetIntegration
from Utilities.ILASPSyntax import createTimeRange


def createExpressivityConstraint(sentence: Question):
    questionWithAnswers = sentence.getQuestionWithAnswers()
    constraint = ":- "
    for predicate in questionWithAnswers:
        if questionWithAnswers.index(predicate) != 0:
            constraint += ', '
        constraint += predicate
    constraint += ', '
    constraint += sentence.getEventCalculusRepresentation()[0][0]
    for answer in sentence.getAnswer():
        constraint += ', ' + 'V1 != ' + answer.lower()
    return constraint


def createYesNoMaybeRule(question: Question):
    representation = question.getEventCalculusRepresentation()[0][0]
    if "no" in question.getAnswer():
        return ":- " + representation
    else:
        return representation


def createChoiceRule(fluents, statement, eventCalculusUsage=False):
    if len(fluents) == 1:
        if statement.negatedVerb and not eventCalculusUsage:
            return ":- " + fluents[0]
        return fluents[0]
    rule = "1{"
    for fluent in fluents:
        if rule[-1] != "{":
            rule += ";"
        rule += fluent
    rule += "}1"
    return rule


def createExpressivityFile(story: Story, corpus: Corpus, filename='/tmp/ILASPExpressivityFile.las'):
    file = open(filename, 'w')
    for rule in corpus.backgroundKnowledge:
        file.write(rule)
        file.write('\n')
    inclusionOrExclusion = []
    for sentence in story:
        representation = sentence.getEventCalculusRepresentation()
        if isinstance(sentence, Question):
            if sentence.isYesNoMaybeQuestion():
                rule = createYesNoMaybeRule(sentence)
                if "yes" in sentence.getAnswer() or "no" in sentence.getAnswer():
                    file.write(rule)
                    file.write('.\n')
                else:
                    file.write("0{" + sentence.getEventCalculusRepresentation()[0][0] + "}1")
                    file.write('.\n')
                    inclusionOrExclusion.append(rule)
            else:
                questionWithAnswers = sentence.getQuestionWithAnswers()
                for predicate in questionWithAnswers:
                    file.write(predicate)
                    file.write('.\n')
                expressivityConstraint = createExpressivityConstraint(sentence)
                file.write(expressivityConstraint)
                file.write('.\n')
        else:
            for i in range(0, len(representation)):
                choiceRule = createChoiceRule(representation[i], sentence, eventCalculusUsage=True)
                file.write(choiceRule)
                file.write('.\n')
    file.write(createTimeRange(len(story)))
    file.write('.\n')
    if not inclusionOrExclusion:
        file.write(createPositiveExample())
        return filename
    for element in inclusionOrExclusion:
        file.write(createPositiveExample(inclusion=element))
        file.write(createPositiveExample(exclusion=element))
    return filename


def createPositiveExample(inclusion="", exclusion=""):
    return "#pos({" + inclusion + "},{" + exclusion + "},{" + "}).\n"


def isUnsatisfiable(output):
    return "UNSATISFIABLE" in output


def runILASP(filename):
    command = "ILASP --version=4 " + filename
    output = os.popen(command).read()
    return output


def isEventCalculusNeeded(corpus: Corpus):
    semanticNetwork = ConceptNetIntegration()
    for story in corpus:
        for sentence in story:
            for rule in sentence.constantModeBias:
                if semanticNetwork.hasTemporalAspect(rule.split(',')[1].split(')')[0]):
                    return False
    for story in corpus:
        filename = createExpressivityFile(story, corpus)
        answerSets = runILASP(filename)
        if isUnsatisfiable(answerSets):
            os.remove(filename)
            return True
        os.remove(filename)
    return False
