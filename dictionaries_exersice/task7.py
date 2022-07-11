number = int(input())
synonyms = dict()
for words in range(number):
    word = input()

    if word not in synonyms:
        synonyms[word] = []

    synonyms[word].append(input())

for keys in synonyms:
    print(f"{keys} - {', '.join(synonyms[keys])}")

