from StoryStructure.Question import Question
from StoryStructure.Sentence import Sentence

def eventCalculusAxioms():
    axiom1 = "holdsAt(F,T+1) :- initiatedAt(F,T), time(T)."
    axiom2 = "holdsAt(F,T+1) :- holdsAt(F,T), not terminatedAt(F,T), time(T)."
    axioms: set[str] = set()
    axioms.add(axiom1)
    axioms.add(axiom2)
    return axioms

def countBackgroundKwnoledge():
    axiom1 = "carriedItems(X,N,T) :- holdsAt(carry(X,_),T), int(N), N #count{Z: holdsAt(carry(X,Z),T)} N."
    axiom2 = "int(0..5)."
    axioms: set[str] = set()
    axioms.add(axiom1)
    axioms.add(axiom2)
    return axioms

def holdsAt(fluent, time):
    return "holdsAt(" + fluent + "," + str(time) + ")"


def happensAt(fluent, time):
    return "happensAt(" + fluent + "," + str(time) + ")"


def initiatedAt(fluent, time):
    return "initiatedAt(" + fluent + "," + str(time) + ")"


def terminatedAt(fluent, time):
    return "terminatedAt(" + fluent + "," + str(time) + ")"

def createTimeRange(time: int):
    return 'time(1..' + str(time) + ')'


def wrap(statement: Sentence):
    fluents = statement.getFluents()
    eventCalculusPredicates = []
    time = statement.getLineID()
    for i in range(0, len(fluents)):
        currentECPredicates = []
        for j in range(0, len(fluents[i])):
            fluent = fluents[i][j]
            predicate = fluent.split("(")[0].split('_')[0]
            if predicate == "be" or isinstance(statement, Question):
                if statement.negatedVerb:
                    eventCalculus = terminatedAt(fluent, time)
                elif isinstance(statement, Question):
                    eventCalculus = holdsAt(fluent, time)
                else:
                    eventCalculus = initiatedAt(fluent, time)
            else:
                eventCalculus = happensAt(fluent, time)
            currentECPredicates.append(eventCalculus)
        eventCalculusPredicates.append(currentECPredicates)
    statement.setEventCalculusRepresentation(eventCalculusPredicates)

