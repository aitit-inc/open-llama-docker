import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

# Use this if downloading model at runtime
# model_path = 'openlm-research/open_llama_3b'
# model_path = 'openlm-research/open_llama_7b'

# Use this if load model offline
# Need to download and place the model to the path
model_path = '/models/models--openlm-research--open_llama_3b/snapshots/8fcddba529aef0eda7293cc9a4171a3994648d2e'
# model_path = '/models/models--openlm-research--open_llama_7b/snapshots/fbf8f0ff929f7abc0b98dcb003e3a73069f8207e'

tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16, device_map='auto',
)

prompt = 'Q: What is the largest animal?\nA:'
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=32
)
print(tokenizer.decode(generation_output[0]))
