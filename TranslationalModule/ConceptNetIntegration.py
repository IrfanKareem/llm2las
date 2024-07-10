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