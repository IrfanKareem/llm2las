from StoryStructure.Sentence import Sentence


class Question(Sentence):
    def __init__(self, text, lineId, answer=None, hints=None):
        Sentence.__init__(self, text, lineId)
        if answer:
            self.answer = [ans.lower() for ans in answer]
        else:
            self.answer = None
        self.hints = hints
        self.variableTypes = {}

    def getAnswer(self):
        return self.answer

    def setAnswer(self, answer):
        self.answer = answer

    def getHints(self):
        return self.hints

    def isCorrectAnswer(self, answer):
        return set(answer) == set(self.answer)

    def getQuestionWithAnswers(self, eventCalculusNeeded=True):
        questionWithAnswer = []
        for answer in self.getAnswer():
            example = self.answerFiller(answer, eventCalculusNeeded)
            questionWithAnswer.append(example)
        return questionWithAnswer

    def createPartialInterpretation(self, answers=None):
        if self.isYesNoMaybeQuestion():
            ECInterpretation = '{' + self.eventCalculusRepresentation[0][0] + '}'
            nonECInterpretation = '{' + self.getFluents().copy()[0][0] + '}'
            return nonECInterpretation, ECInterpretation
        ECInterpretation = '{'
        for answer in answers:
            if answers.index(answer) != 0:
                ECInterpretation += ','
            example = self.answerFiller(answer, eventCalculusNeeded=True)
            ECInterpretation += example
        ECInterpretation += '}'
        nonECInterpretation = '{'
        for answer in answers:
            if answers.index(answer) != 0:
                nonECInterpretation += ','
            example = self.answerFiller(answer, eventCalculusNeeded=False)
            nonECInterpretation += example
        nonECInterpretation += '}'
        return nonECInterpretation, ECInterpretation

    def answerFiller(self, answer, eventCalculusNeeded):
        if eventCalculusNeeded:
            representation = self.getEventCalculusRepresentation()[0][0]
        else:
            representation = self.getFluents()[0][0]
        representationWithAnswer = representation.replace("V1", answer.lower())
        return representationWithAnswer

    def isYesNoMaybeQuestion(self):
        if self.answer:
            return "yes" in self.answer or "no" in self.answer or "maybe" in self.answer
        firstWord = self.doc[0].lemma_.lower()
        return firstWord == "be" or firstWord == "do" or firstWord == "have"

    def isHowManyQuestion(self):
        return "how many" in self.text.lower()

    def isWhereQuestion(self):
        return "where" in self.text.lower()

    def isWhatQuestion(self):
        return "what" in self.text.lower()

    def isWhoQuestion(self):
        return "who" in self.text.lower()

    def isWhyQuestion(self):
        return "why" in self.text.lower()

