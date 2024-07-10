# This is repository for the *paper Using Learning from Answer Sets for Robust Question Answering with LLM* submitted in conference LPNMR 2024.

# LLM2LAS
A tool Learning from Answer Sets for Robust Question Answering with Large Language Model (LLM)
## Dependencies
- Hugging Face LLM Model: falcon-7b-instruct
- ILASP version 4.4.0 
- clingo 5.6.2
- transformers 4.39.3
- pytorch 2.4.0
- spaCy
- Djano framework
- ***install requirement.txt*** in local machine
### Install LLM Module
-  LLM model `"tiiuae/falcon-7b-instruct"` accessed by `access_token = "Your HuggingFace Access Key"` which takes around *15GB* disk space, install LLM module on GPU server with `django framework`
### Install ReasoningModule 
-Install clingo v5.6.2 in local machine 
### Install LearningModule
-install ILASP v4.4.0 local machine with good RAM (0ur case 16GB)and CPU.

## How to RUN
- After installing the dependencies at GPU server and local system.
- RUN Django framework at GPU server by using command
`python manage.py runserver`
- update in BasicParser.py `LLM_SERVICE_URL = "http://YOUR_IP_ADDRESS:YOUR_PORT/logic/generate/"` to get the response from GPU server application
- use the following command to RUN LLM2LAS 
 `python -m SystemPipeline.OverallPipeline -component=dataset --train=/Your path/bAbi/qa1_train.txt --test=/Your path/bAbi/qa1_test.txt -r=EventCalculus -n=1000 --taskId=1`
- command discription specify the train and test file location with flags ***--train*** and ***--test***, with flag ***-r*** specify the mode of representation as it can be   ***EventCalculus*** or ***Fluent***, flag ***-n*** specify the number of training and testing examples and flag ***--taskId*** indicates the bAbI dataset task number as *taskId* can be *(1,6,8,9,10,11,12,13,14,15,16,18,20)*