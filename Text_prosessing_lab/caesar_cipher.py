text = input()
cipher = ""
for char in range(0, len(text)):
    letter = ord(text[char]) + 3
    cipher += chr(letter)

print(cipher)