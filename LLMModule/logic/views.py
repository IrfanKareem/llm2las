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
model_name = "tiiuae/falcon-7b-instruct" 
access_token = "Your HuggingFace Access Key" 
prompt = prompts[1]
lm_model = LanguageModel(model_name, access_token, prompt)


@api_view(['POST'])
def generate_response(request):
    sentence = request.data.get('sentence')
    taskId = request.data.get('taskId')
    if taskId not in list(prompts.keys()):
        return None 
    lm_model.update_prompt(prompts[taskId])
    response = lm_model.generate(sentence)
    generated_text = response[0]['generated_text']
    # Extract the last two lines for sentence and semantic parse
    your_turn_idx = generated_text.find('Your turn')
    if your_turn_idx > 0:
        target_answer = generated_text[your_turn_idx:].split('\n')
        if len(target_answer) > 2:
            raw = target_answer[2].replace("Semantic parse:", "")
            return Response({
                "sentence": sentence,
                "semantic_parse": raw.strip()
            })

    return Response({
        "sentence": sentence,
        "semantic_parse": ""
    })
