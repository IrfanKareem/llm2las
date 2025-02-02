import os
#import torch
#from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from openai import OpenAI

class LanguageModel:
    def __init__(self, model_name, access_token, prompt, api_url):  
        self.model_name = model_name
        self.prompt = prompt
        self.client = OpenAI(
    	    base_url = api_url,
    	    api_key = access_token
    )

    def update_prompt(self, new_prompt):
        self.prompt = new_prompt
    
    def generate(self, sentence, max_length=1740, do_sample=False, temperature=0.8, top_p=0.9, num_return_sequences=1):   
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages = [
                { 
                    "role": "system", 
                    "content": [
                        {
                            "type": "text",
                            "text": "Hello, your job is to semantic parse some sentences and questions into a first-order logic predicate form." 
                        }
                    ] 
                },
                { 
                    "role": "user", 
                    "content": [
                        {
                            "type": "text", 
                            "text": self.prompt.replace("{{sentence}}", sentence)
                        }
                    ]
                }
            ],
            response_format={
                "type": "text"
            },
            temperature=temperature,
            max_completion_tokens=2048,
            top_p=top_p,
        )
        return response.choices[0].message.content
    
    def generate_mb(self, sentence, fluent, max_length=2048, do_sample=False, temperature=0.5, top_p=0.5, num_return_sequences=1):   
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages = [
                { 
                    "role": "system", 
                    "content": [
                        {
                            "type": "text",
                            "text": "Hello, you are a semantic parser assistant in the propositional logic field. Your job is to semantic parse some sentences and questions into a mode bias representation." 
                        }
                    ] 
                },
                { 
                    "role": "user", 
                    "content": [
                        {
                            "type": "text", 
                            "text": self.prompt.replace("{{sentence}}", sentence).replace("{{fluent}}", fluent)
                        }
                    ]
                }
            ],
            response_format={
                "type": "text"
            },
            temperature=temperature,
            max_completion_tokens=max_length,
            top_p=top_p
        )
        return response.choices[0].message.content

# class LanguageModel:
#     def __init__(self, model_name, access_token, prompt):  
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)
#         self.model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=access_token)
#         self.prompt = prompt
#         self.text_generation = pipeline(
#             "text-generation",
#             model=self.model,
#             tokenizer=self.tokenizer,
#             torch_dtype=torch.bfloat16,
#             trust_remote_code=True,
#             output_scores=True,
#             #device=0
#         )

#     def update_prompt(self, new_prompt):
#         self.prompt = new_prompt
    
#     def generate(self, sentence, max_length=1740, do_sample=False, temperature=0.9, top_p=0.85, num_return_sequences=1):   
#         complete_prompt = self.prompt + "Sentence: " + sentence
#         return self.text_generation(
#             complete_prompt,
#             max_length=max_length,
#             do_sample=do_sample,
#             temperature=temperature,
#             top_p=top_p,
#             num_return_sequences=num_return_sequences,
#             eos_token_id=self.tokenizer.eos_token_id, 
#             pad_token_id=self.tokenizer.eos_token_id   
#         )


