import re

with open('dataset/the-verdict.txt',"r",encoding="utf-8") as f:
    raw_text = f.read()

print(len(raw_text))

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
print(len(preprocessed))

# Basic tokenizer is now ready. LLMs use a different variation called byte pair encoding