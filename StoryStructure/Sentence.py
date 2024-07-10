class Sentence:
    def __init__(self, lineId, text):
        self.text = text
        self.lineId = int(lineId)
        self.fluents = list(list())
        self.eventCalculusRepresentation = list(list())
        self.modeBiasFluents = list(list())
        self.constantModeBias = set()
        self.negatedVerb = False
        self.doc = None

    def __eq__(self, other):
        return self.text == other.text and self.lineId == other.lineId

    def getFluentBase(self):
        return self.fluents[0][0].split('(')[0]

    def addConstantModeBias(self, constantModeBias):
        self.constantModeBias.add(constantModeBias)

    def getConstantModeBias(self):
        return self.constantModeBias

    def getText(self):
        return self.text

    def getLineID(self):
        return self.lineId

    def getEventCalculusRepresentation(self):
        return self.eventCalculusRepresentation

    def setEventCalculusRepresentation(self, representation):
        self.eventCalculusRepresentation = representation

    def setFluents(self, fluents):
        self.fluents = fluents

    def getFluents(self):
        return self.fluents

    def setModeBiasFluents(self, modeBiasFluents):
        self.modeBiasFluents = modeBiasFluents

    def getModeBiasFluents(self):
        return self.modeBiasFluents

    def __str__(self):
        return self.text
