data = input()

words = dict()

for char in data:
    if char != " ":
        if char not in words:
            words[char] = 0

        words[char] += 1

for text, number in words.items():
    print(f"{text} -> {number}")
