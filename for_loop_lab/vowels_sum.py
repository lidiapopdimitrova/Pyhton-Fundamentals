text = input()
total = 0
for ch in range(0, len(text)):
    if text[ch] == 'a':
        total += 1
    if text[ch] == 'e':
        total += 2
    if text[ch] == 'i':
        total += 3
    if text[ch] == 'o':
        total += 4
    if text[ch] == 'u':
        total += 5
print(total)


