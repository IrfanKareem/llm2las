TASK_ID=$1
EXAMPLES=$2
python -m SystemPipeline.OverallPipeline -component=dataset --train=./bAbi/qa${TASK_ID}_train.txt --test=./bAbi/qa${TASK_ID}_test.txt -r=EventCalculus -n=$EXAMPLES --taskId=$TASK_ID --ilasp_version=2i --dataset-shuffle-seed=89
