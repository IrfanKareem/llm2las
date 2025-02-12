from .AbstractILPSyntax import AbstractILPSyntax


###leaving for temporary compatibility
def maxVariables(number):
    return "#maxv(" + str(number) + ").\n"

def varWrapping(tag):
    return "var(" + tag + ")"

def constWrapping(tag):
    return "const(" + tag + ")"

def createConstantTerm(tag, noun):
    return "#constant(" + tag + "," + noun.lower() + ")."

class ILASPSyntaxCreator(AbstractILPSyntax):
    
    def createTimeRange(self, time: int):
        return 'time(1..' + str(time) + ')'

    def modeHWrapping(self, predicate):
        return "#modeh(" + predicate + ")."

    def modeBWrapping(self, predicate):
        return "#modeb(" + predicate + ")."

    def createBias(self, predicate):
        return "#bias(\":-" + predicate + ".\")."

    def maxVariables(self, number):
        return "#maxv(" + str(number) + ").\n"

    def varWrapping(self, tag):
        return "var(" + tag + ")"

    def constWrapping(self, tag):
        return "const(" + tag + ")"

    def createConstantTerm(self, tag, noun):
        return "#constant(" + tag + "," + noun.lower() + ")."

    def numberOfArguments(self, fluent):
        return len(fluent.split(','))

    def addConstraints(self, modeBiasFluent):
        constraints = ",(positive"
        if self.numberOfArguments(modeBiasFluent) == 2:
            constraints += ", anti_reflexive)"
        else:
            constraints += ")"
        newMBFluent = modeBiasFluent[:-2]
        newMBFluent += constraints + ")."
        return newMBFluent