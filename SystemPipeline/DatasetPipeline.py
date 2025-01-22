import time
from DatasetReader.bAbIReader import bAbIReader
from LearningModule.learner import Learner, LearnerV2
from LearningModule.modeBiasGenerator import ModeBiasGenerator
from ReasoningModule.reasoner import Reasoner
from StoryStructure.Corpus import pruneCorpus
from StoryStructure.Question import Question
from TranslationalModule.ChoiceRulesChecker import choiceRulesPresent
from TranslationalModule.DatasetParser import DatasetParser
from TranslationalModule.ExpressivityChecker import isEventCalculusNeeded
import logging

logging.basicConfig(level=logging.INFO, filename="answered.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")

MAX_EXAMPLES = 10000


def DatasetPipeline(trainCorpus, testCorpus, numExamples=MAX_EXAMPLES, useSupervision=False,
                    useExpressivityChecker=(True, None), taskId=1, ilasp_version='4',dataset_shuffle_seed=0,use_baked_las_file=False, shortest_stories_first_heuristics=False):
    startTime = time.time()

    if numExamples < MAX_EXAMPLES:
        trainCorpus = pruneCorpus(trainCorpus, numExamples)
        trainCorpus.shuffle(dataset_shuffle_seed)

        testCorpus = pruneCorpus(testCorpus, numExamples)
    print("starting parsing.... " + str(time.time()))
    print("total number of stories: ", len(trainCorpus.stories))
    print("dataset shuffle seed: ", dataset_shuffle_seed)

    if shortest_stories_first_heuristics:
        trainCorpus.sort_stories_by_timestamps(reverse=True)

    DatasetParser(trainCorpus, testCorpus, useSupervision=useSupervision, taskId=taskId)

    parseEndTime = time.time()

    reasoner = Reasoner(trainCorpus)

    learner = LearnerV2(trainCorpus, useSupervision=useSupervision, ilasp_version=ilasp_version)

    if useExpressivityChecker[0]:
        trainCorpus.isEventCalculusNeeded = isEventCalculusNeeded(trainCorpus)
    else:
        trainCorpus.isEventCalculusNeeded = useExpressivityChecker[1]

    trainCorpus.choiceRulesPresent = choiceRulesPresent(trainCorpus)

    train(trainCorpus, reasoner, learner, useSupervision)
    learningTime = time.time()

    numQuestions = 0
    numCorrect = 0
    
    for story in testCorpus:
        print("-----------------")
        for sentence in story:
            print(sentence.text)
            if isinstance(sentence, Question):
                numQuestions += 1
                answerToQuestion = reasoner.computeAnswer(sentence, story)                
                print(sentence.answer)
                print(' '.join(answerToQuestion))
                if sentence.isCorrectAnswer(answerToQuestion):
                    numCorrect += 1
        print("-----------------")

    return numCorrect / numQuestions, parseEndTime - startTime, learningTime - parseEndTime


def train(corpus, reasoner, learner, useSupervision):
    modeBiasGenerator = ModeBiasGenerator(corpus, useSupervision)
    modeBiasGenerator.assembleModeBias()
    for story in corpus:
        for sentence in story:
            if isinstance(sentence, Question):
                answerToQuestion = reasoner.computeAnswer(sentence, story)   
                logging.info("ANSWERED QUESTION: " + sentence.text + " ANSWER: " + ', '.join(answerToQuestion) + " -- REAL: " +', '.join(sentence.answer))             
                if not sentence.isCorrectAnswer(answerToQuestion):                  
                    logging.info("NEED TO LEARN****") 
                    learner.learn(sentence, story, answerToQuestion)
                print("------------------------------------")
