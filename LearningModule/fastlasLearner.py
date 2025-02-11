import os
from Utilities.ILASPSyntax import AbstractILPSyntax
from pathlib import Path 
from LearningModule.learner import LearnerV2
from Utilities.FastLASSyntax import FastLASSyntaxCreator

def check_file_not_empty(file):
    contents = Path(file).open('r').read()
    if len(contents.strip()) == 0:
        raise RuntimeError("Unexpected empty file:", file)

def isSatisfiable(hypotheses):
    is_unsatisfiable = "UNSATISFIABLE" in hypotheses
    return not is_unsatisfiable
    
class FastLASLearner(LearnerV2):
    def __init__(self, 
                 corpus,
                 language_bias=Path('~/bias.las').expanduser(),
                 examples=Path('~/examples.las').expanduser(),
                 background_knowledge=Path('~/background.las').expanduser(),
                 cache=Path('~/fastlas_cache').expanduser(),
                 useSupervision=False,
                 syntax_creator=None
    ):
        super().__init__(corpus, language_bias, examples, background_knowledge, cache, useSupervision)
        self.syntax_creator: AbstractILPSyntax = FastLASSyntaxCreator() 

    def createLearningFile(self):
        with open(self.language_bias_file, 'w') as lang_bias, open(self.examples_file, 'w') as examples, open(self.background_knowledge_file, 'w') as background_knowledge:
            if self.corpus.isEventCalculusNeeded:
                for rule in self.corpus.backgroundKnowledge:
                    background_knowledge.write(rule)
                    background_knowledge.write('\n')
                for bias in self.corpus.ECModeBias:
                    lang_bias.write(bias)
                    lang_bias.write('\n')

            else:
                for bias in self.corpus.nonECModeBias:
                    lang_bias.write(bias)
                    lang_bias.write('\n')

            for constantBias in self.corpus.constantModeBias:
                lang_bias.write(constantBias)
                lang_bias.write('\n')

            lang_bias.write(self.syntax_creator.maxVariables(self.heuristics.maximumNumberOfVariables()))

            if self.corpus.isEventCalculusNeeded:
                for example in self.corpus.eventCalculusExamples:
                    examples.write(example)
                    examples.write('\n')
            else:
                for example in self.corpus.nonEventCalculusExamples:
                    examples.write(example)
                    examples.write('\n')
            self.currentExamplesIndex = len(self.corpus.nonEventCalculusExamples)

    def solveILASPTask(self):
        command = f"FastLAS --nopl --force-safety --write-cache={self.caching} {self.background_knowledge_file} {self.examples_file} {self.language_bias_file}"
        print("Calling FastLAS: ", command)
        from datetime import datetime
        print("STARTED AT: ", datetime.now().strftime("%H:%M:%S"))
        output = os.popen(command).read()
        print("FastLAS OUTPUT:")
        print(output)
        ans = self.processILASP(output)
        print("FINISHED AT: ", datetime.now().strftime("%H:%M:%S"))
        if isSatisfiable(ans):
            return ans
        else:
            return {"UNSATISFIABLE"}
