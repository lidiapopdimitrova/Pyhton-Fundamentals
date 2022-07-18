import re

text = input()
cool_threshold = 1

pattern_emoji = r"(::|\*\*)([A-Z][a-z]{2,})\1"
pattern_numbers = r"\d"

valid_emojis = re.findall(pattern_emoji, text)
valid_numbers = re.findall(pattern_numbers, text)
valid_emojis1 = re.finditer(pattern_emoji, text)

for i in valid_numbers:
    cool_threshold *= int(i)
print(f"Cool threshold: {cool_threshold}")

emoji_names = list()
for matches in valid_emojis:
    emoji_names.append(matches[1])

print(f"{len(emoji_names)} emojis found in the text. The cool ones are:")

for names in valid_emojis1:
    coolness = 1
    for char in names.group(2):
        coolness += ord(char)
    if coolness >= cool_threshold:
        print(names.group())



