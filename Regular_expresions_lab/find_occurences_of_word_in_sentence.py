import re

text = input()
searches_word = input()

pattern = fr"\b{searches_word}\b"
matches = re.findall(pattern, text, flags=re.I)

print(len(matches))