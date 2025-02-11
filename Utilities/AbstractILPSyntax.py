from abc import ABC, abstractmethod

class AbstractILPSyntax(ABC):

    @abstractmethod
    def createTimeRange(self, time: int):
        pass

    @abstractmethod
    def modeHWrapping(self, predicate):
        pass

    @abstractmethod
    def modeBWrapping(self, predicate):
        pass

    @abstractmethod
    def createBias(self, predicate):
        pass

    @abstractmethod
    def maxVariables(self, number):
        pass

    @abstractmethod
    def varWrapping(self, tag):
        pass

    @abstractmethod
    def constWrapping(self, tag):
        pass

    @abstractmethod
    def createConstantTerm(self, tag, noun):
        pass

    @abstractmethod
    def numberOfArguments(self, fluent):
        pass

    @abstractmethod
    def addConstraints(self, modeBiasFluent):
        pass