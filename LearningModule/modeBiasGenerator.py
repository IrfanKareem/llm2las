from StoryStructure.Question import Question
from StoryStructure.Sentence import Sentence
from TranslationalModule.EventCalculus import initiatedAt, terminatedAt, holdsAt, happensAt
from Utilities.ILASPSyntax import varWrapping, modeHWrapping, modeBWrapping


class ModeBiasGenerator:
    def __init__(self, corpus, useSupervision=False):
        self.corpus = corpus
        self.useSupervision = useSupervision

    @staticmethod
    def generateBeAndQuestionBias(modeBiasFluent, isQuestion=True):
        nonECBias = set()
        ECBias = set()
        time = varWrapping("time")
        if isQuestion:
            ECBias.add(modeHWrapping(initiatedAt(modeBiasFluent, time)))
            ECBias.add(modeHWrapping(terminatedAt(modeBiasFluent, time)))
            nonECBias.add(modeHWrapping(modeBiasFluent))
        else:
            ECBias.add(modeBWrapping(initiatedAt(modeBiasFluent, time)))
            nonECBias.add(modeBWrapping(modeBiasFluent))
        ECBias.add(modeBWrapping(holdsAt(modeBiasFluent, time)))
        return nonECBias, ECBias

    @staticmethod
    def generateNonBeBias(modeBiasFluent):
        nonECBias = set()
        ECBias = set()
        time = varWrapping("time")
        ECBias.add(modeBWrapping(happensAt(modeBiasFluent, time)))
        nonECBias.add(modeBWrapping(modeBiasFluent))
        return nonECBias, ECBias

    def addStatementModeBias(self, statement: Sentence):
        modeBiasFluents = statement.getModeBiasFluents()
        ECModeBias = set()
        nonECModeBias = set()
        for i in range(0, len(modeBiasFluents)):
            for j in range(0, len(modeBiasFluents[i])):
                modeBiasFluent = modeBiasFluents[i][j]
                predicate = modeBiasFluent.split('(')[0].split('_')[0]
                if predicate == "be" or isinstance(statement, Question):
                    newNonECModeBias, newECModeBias = self.generateBeAndQuestionBias(modeBiasFluent,
                                                                                     isinstance(statement, Question))
                else:
                    newNonECModeBias, newECModeBias = self.generateNonBeBias(modeBiasFluent)
                ECModeBias.update(newECModeBias)
                nonECModeBias.update(newNonECModeBias)
        return nonECModeBias, ECModeBias

    def addModeBias(self, sentence: Sentence):
        nonECModeBias, ECModeBias = self.addStatementModeBias(sentence)
        self.corpus.updateECModeBias(ECModeBias)
        self.corpus.updateNonECModeBias(nonECModeBias)
        self.corpus.updateConstantModeBias(sentence.getConstantModeBias())

    # This function is used as a work around for a bug in ILASP (version 4.1.1) which causes only a fraction of the
    # hypothesis space given by the mode declarations to be generated. The bug should be resolved in the next release
    # of ILASP, which will render this function unnecessary.
    def checkAndReassembleModeBias(self):
        nounsInHead = False
        properNounsInHead = False
        nounsInBody = False
        properNounsInBody = False
        for bias in self.corpus.nonECModeBias:
            if "modeh" in bias:
                if "var(nn)" in bias:
                    nounsInHead = True
                if "var(nnp)" in bias:
                    properNounsInHead = True
            else:
                if "var(nn)" in bias:
                    nounsInBody = True
                if "var(nnp)" in bias:
                    properNounsInBody = True
        if nounsInBody and properNounsInHead and not nounsInHead:
            nonECModeBiasCopy = self.corpus.nonECModeBias.copy()
            self.corpus.nonECModeBias = set()
            for bias in nonECModeBiasCopy:
                bias = bias.replace("nnp", "nn")
                self.corpus.nonECModeBias.add(bias)
            ECModeBiasCopy = self.corpus.ECModeBias.copy()
            self.corpus.ECModeBias = set()
            for bias in ECModeBiasCopy:
                bias = bias.replace("nnp", "nn")
                self.corpus.ECModeBias.add(bias)
        elif properNounsInBody and not properNounsInHead:
            nonECBias, ECBias = self.generateBeAndQuestionBias("fluent1(var(nnp),var(nn))")
            self.corpus.nonECModeBias.update(nonECBias)
            self.corpus.ECModeBias.update(ECBias)
            nonECBias, ECBias = self.generateBeAndQuestionBias("fluent2(var(nnp),var(nn))")
            self.corpus.nonECModeBias.update(nonECBias)
            self.corpus.ECModeBias.update(ECBias)

    def assembleModeBias(self):
        if self.useSupervision:
            for story in self.corpus:
                for sentence in story:
                    if isinstance(sentence, Question):
                        for hint in sentence.getHints():
                            self.addModeBias(story.get(int(hint) - 1))
                        self.addModeBias(sentence)
        else:
            for story in self.corpus:
                for sentence in story:
                    self.addModeBias(sentence)
        self.checkAndReassembleModeBias()
