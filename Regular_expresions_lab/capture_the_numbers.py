import re

line = input()
pattern = r"\d+"
while True:
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(" ".join(matches), end=" ")
        line = input()
    else:
        break


