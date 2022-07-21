import re
count_of_inputs = int(input())

pattern = r"^(\$|\%)([A-Z][a-z]{2,})\1\:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"

for _ in range(count_of_inputs):
    message = input()
    matches = re.finditer(pattern, message)
    valid = []
    for match in matches:
        valid.append(match.group())
        decode = chr(int(match.group(3))) + chr(int(match.group(4))) + chr(int(match.group(5)))
        print(f"{match[2]}: {decode}")
    if message not in valid:
        print("Valid message not found!")

