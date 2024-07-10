from StoryStructure.Corpus import Corpus


def choiceRulesPresent(corpus: Corpus):
    for story in corpus:
        for sentence in story:
            representation = sentence.getFluents()
            for disjunctiveClause in representation:
                if len(disjunctiveClause) >1:
                    return True
    return False
