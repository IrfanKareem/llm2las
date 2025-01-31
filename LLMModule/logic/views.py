from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import LlmSerializer
from .llm import LanguageModel
from rest_framework.response import Response
import re
from .llm_prompts import prompts

# Initialize the model here (you can modify parameters as needed)   
model_name = "llama3.3:70b" 
access_token = "Your HuggingFace Access Key"
API_URL = "http://172.20.64.1:11434/v1"
prompt = prompts[1]
lm_model = LanguageModel(model_name, access_token, prompt, API_URL)


@api_view(['POST'])
def generate_response(request):
    sentence = request.data.get('sentence')
    taskId = request.data.get('taskId')
    if taskId not in list(prompts.keys()):
        return None 
    lm_model.update_prompt(prompts[taskId])
    response = lm_model.generate(sentence)
    # generated_text = response[0]['generated_text']
    # Extract the last two lines for sentence and semantic parse
    parsing_idx = response.find('Semantic parse:')
    if parsing_idx != -1:
        parsed_predicate = re.sub(r"Semantic parse:\s*","", response[parsing_idx:]).replace(".","")
        #parsed_predicate = re.sub(r"\s+","", parsed_predicate)
        parsed_predicate = re.sub(r"\n","", parsed_predicate)
        if len(parsed_predicate) != 0:
            return Response({
                "sentence": sentence,
                "semantic_parse": parsed_predicate.strip()
            })

    return Response({
        "sentence": sentence,
        "semantic_parse": ""
    })

@api_view(['POST'])
def generate_mb(request):
    sentence = request.data.get('sentence')
    fluent = request.data.get('fluent')
    if not fluent or not sentence:
        return None

    lm_model.update_prompt(prompts[0])
    response = lm_model.generate_mb(sentence, fluent)
    # generated_text = response[0]['generated_text']
    # Extract the last two lines for sentence and semantic parse
    parsing_idx = response.find('Mode bias:')
    if parsing_idx != -1:
        parsed_predicate = re.sub(r"Mode bias:\s*","", response[parsing_idx:]).replace(".","")
        print(parsed_predicate)
        #parsed_predicate = re.sub(r"\s+","", parsed_predicate)
        parsed_predicate = re.sub(r"\n","", parsed_predicate)
        if len(parsed_predicate) != 0:
            return Response({
                "sentence": sentence,
                "semantic_parse": parsed_predicate.strip()
            })

    return Response({
        "sentence": sentence,
        "semantic_parse": ""
    })

