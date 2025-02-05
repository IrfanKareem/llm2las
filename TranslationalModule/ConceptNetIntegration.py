import requests


class ConceptNetIntegration:
    def __init__(self):
        self.baseAddress = 'http://api.conceptnet.io/'
        self.isArelation = 'query?rel=/r/IsA'
        self.start = '&start=/c/en/'
        self.end = '&end=/c/en/'


    def hasTemporalAspect(self, word):
        query = self.baseAddress + self.isArelation + self.start + word
        obj = requests.get(query).json()
        for edge in obj['edges']:
            end = edge["end"]
            if "day" in end["label"]:
                return True
        return False
    
    def isA(self, word, concept, moreSearches=True):
        start = self.start + word.replace(" ", "_")
        other = self.end + concept.replace(" ", "_")
        query = self.baseAddress + self.isArelation + start + other
        obj = requests.get(query).json()
        if obj['edges']:
            return True
        query = self.baseAddress + self.isArelation + start
        obj = requests.get(query).json()
        if moreSearches:
            for edge in obj['edges']:
                if concept in edge['end']['label']:
                    return True
                if self.isA(edge['end']['label'], concept, False):
                    return True
        return False