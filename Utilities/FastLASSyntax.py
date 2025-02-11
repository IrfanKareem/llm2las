from .ILASPSyntax import ILASPSyntaxCreator


class FastLASSyntaxCreator(ILASPSyntaxCreator):
    
    def createConstantTerm(self, tag, noun):
        return f"{tag}({noun})."
