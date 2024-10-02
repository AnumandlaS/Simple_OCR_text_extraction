from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('srimanth-d/GOT_CPU', trust_remote_code=True)
model = AutoModel.from_pretrained('srimanth-d/GOT_CPU', trust_remote_code=True, low_cpu_mem_usage=True, use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
model = model.eval()
#'srimanth-d/GOT_CPU':- I am using this as I got its refernce from the official page of got_ocr_model, in the comments.

# input your test image
image_file = 'ocr_test1.png'
# plain texts - OCR
res = model.chat(tokenizer, image_file, ocr_type='ocr')

print(res)
#requirements:
# !pip install torch
# !pip install torchvision
# !pip install transformers
# !pip install tiktoken
# !pip install verovio
# !pip install accelerate
# !pip install transformers
# !pip install tiktoken
# !pip install verovio
# !pip install Pillow