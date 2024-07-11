## Repository for the Paper: ***Using Learning from Answer Sets for Robust Question Answering with LLM***, LPNMR 2024

## LLM2LAS: A Tool for Learning from Answer Sets for Robust Question Answering with Large Language Models (LLM)

### Dependencies
- **Hugging Face LLM Model**: falcon-7b-instruct
- **ILASP**: Version 4.4.0 
- **Clingo**: Version 5.6.2
- **Transformers**: Version 4.39.3
- **PyTorch**: Version 2.4.0
- **spaCy**
- **Django Framework**
- Install requirements from `requirements.txt` on your local machine

### Installation Instructions

#### LLM Module
1. Install the LLM model `"tiiuae/falcon-7b-instruct"`.
2. Update your Hugging Face account access token in `LLMModule/logic/views.py` by setting `access_token = "Your HuggingFace Access Key"`.
3. Ensure you have around *15GB* of disk space.
4. Install the LLM module on a GPU server using the Django framework.

#### Reasoning Module
- Install Clingo v5.6.2 on your local machine.

#### Learning Module
- Install ILASP v4.4.0 on a local machine with sufficient RAM (16GB recommended) and a good CPU.

### How to Run
1. **Set up the environment**:
   - Install all dependencies on both the GPU server and the local system.

2. **Run the Django Framework**:
   - On the GPU server, start the Django server with the command:
     ```sh
     python manage.py runserver
     ```

3. **Update Configuration**:
   - Modify `TranslationalModule/BasicParser.py` to set `LLM_SERVICE_URL = "http://YOUR_IP_ADDRESS:YOUR_PORT/logic/generate/"` to get responses from the GPU server application.

4. **Run LLM2LAS**:
   - Use the following command to execute LLM2LAS:
     ```sh
     python -m SystemPipeline.OverallPipeline -component=dataset --train=/llm2las/bAbi/qa1_train.txt --test=/llm2las/bAbi/qa1_test.txt -r=EventCalculus -n=1000 --taskId=1
     ```

### Command Description
- `--train`: Specify the path to the training file.
- `--test`: Specify the path to the testing file.
- `-r`: Specify the mode of representation (either `EventCalculus` or `Fluent`).
- `-n`: Specify the number of training and testing examples.
- `--taskId`: Specify the bAbI dataset task number (valid options: 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20).
