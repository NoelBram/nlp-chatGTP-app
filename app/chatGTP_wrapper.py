import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class ChatGPT:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.history = []

    def ask(self, input_text):
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        output_ids = self.model.generate(input_ids, max_length=1000, do_sample=True)
        output_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        self.history.append(input_text)
        self.history.append(output_text)
        return output_text

    def clear_history(self):
        self.history = []
