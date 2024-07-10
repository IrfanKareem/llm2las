import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


class LanguageModel:
    def __init__(self, model_name, access_token, prompt):  
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=access_token)
        self.prompt = prompt
        self.text_generation = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            output_scores=True,
            #device=0
        )

    def update_prompt(self, new_prompt):
        self.prompt = new_prompt
    
    def generate(self, sentence, max_length=1740, do_sample=False, temperature=0.9, top_p=0.85, num_return_sequences=1):   
        complete_prompt = self.prompt + "Sentence: " + sentence
        return self.text_generation(
            complete_prompt,
            max_length=max_length,
            do_sample=do_sample,
            temperature=temperature,
            top_p=top_p,
            num_return_sequences=num_return_sequences,
            eos_token_id=self.tokenizer.eos_token_id, 
            pad_token_id=self.tokenizer.eos_token_id   
        )

