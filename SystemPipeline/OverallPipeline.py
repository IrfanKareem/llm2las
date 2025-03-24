import sys
from DatasetReader.bAbIReader import bAbIReader
from SystemPipeline.DatasetPipeline import DatasetPipeline
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='LLM2LAS')
    parser.add_argument('-component', dest='component', type=str, help='Allowed values: dataset', required=True)
    parser.add_argument('--train', dest='trainset', type=str, help='Training dataset path', required=True)
    parser.add_argument('--test', dest='testset', type=str, help='Test dataset path', required=True)
    parser.add_argument('-s', dest='supervision', help='Use strong supervision for training', action='store_true')
    parser.add_argument('-r', dest='representation', type=str, help='Required representation, either EventCalculus or Fluent', default='Fluent')
    parser.add_argument('-n', '--num-samples', type=int, dest='max_examples', help='test dataset path', default=-1)
    parser.add_argument('--taskId', type=int, dest='taskId', help='bAbi task identifier [1-20]', default=1, required=True)
    parser.add_argument('--ilasp_version', type=str, dest='ilasp_version', help='the ILASP version is one of: 2, 2i, 3, 4', default='4')
    parser.add_argument('--dataset-shuffle-seed', type=int, help="Seed to shuffle the corpus.", default=0)
    parser.add_argument('--learner', dest='learner', type=str, help='Learner to be used, either ILASP or FastLAS', default='ILASP', choices=['ILASP', 'FastLAS'])
    args = parser.parse_args()

    if len(sys.argv) >= 4 and args.component == 'dataset':
        try:           
            trainingFile = args.trainset#sys.argv[2]
            testingFile = args.testset#sys.argv[3]
            useSupervision = args.supervision
            if args.representation == 'EventCalculus':
                useExpressivityChecker = (False, True)
            else:
                useExpressivityChecker = (False, False)
            numExamples = 10000 if args.max_examples == -1 else args.max_examples
            
            trainingCorpus = bAbIReader(trainingFile)
            testingCorpus = bAbIReader(testingFile)
            accuracy, parsingTime, learningTime = DatasetPipeline(trainingCorpus, testingCorpus, 
                                                                  useSupervision=useSupervision, 
                                                                  useExpressivityChecker=useExpressivityChecker,
                                                                  numExamples=numExamples, taskId=args.taskId, ilasp_version=args.ilasp_version, dataset_shuffle_seed=args.dataset_shuffle_seed, learner_system=args.learner)
            print("Parsing Time:", parsingTime, ", Learning Time: ", learningTime, ", Accuracy: ", accuracy)
        except Exception as error:
            print(error.with_traceback())
            print("Something went wrong. Please check all the provided argument are correct and try again")
