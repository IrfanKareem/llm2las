def createTimeRange(time: int):
    return 'time(1..' + str(time) + ')'


def modeHWrapping(predicate):
    return "#modeh(" + predicate + ")."


def modeBWrapping(predicate):
    return "#modeb(" + predicate + ")."


def createBias(predicate):
    return "#bias(\":-" + predicate + ".\")."


def maxVariables(number):
    return "#maxv(" + str(number) + ").\n"


def varWrapping(tag):
    return "var(" + tag + ")"


def constWrapping(tag):
    return "const(" + tag + ")"


def createConstantTerm(tag, noun):
    return "#constant(" + tag + "," + noun.lower() + ")."


def numberOfArguments(fluent):
    return len(fluent.split(','))


def addConstraints(modeBiasFluent):
    constraints = ",(positive"
    if numberOfArguments(modeBiasFluent) == 2:
        constraints += ", anti_reflexive)"
    else:
        constraints += ")"
    newMBFluent = modeBiasFluent[:-2]
    newMBFluent += constraints + ")."
    return newMBFluent
