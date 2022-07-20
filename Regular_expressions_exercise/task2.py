import re

numbers = input()

# valid_numbers = re.findall(r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b", numbers)
# print(", ".join(valid_numbers))


# you can write the regex like that too:
valid_numbers = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", numbers)
# you define a group of elements and search for it later with \1  (group1)
output = list()
for match in valid_numbers:
    output.append(match.group())

print(", ".join(output))
