import re
text = input().lower()
word = input().lower()
pattern = rf"\b{word}\b"
match = re.findall(word, text)
print(len(match))
