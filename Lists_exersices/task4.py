number = int(input())
search_word = input()
strings = list()
filtered = list()

for i in range(number):
    current_string = input()
    strings.append(current_string)
    if search_word in current_string:
        filtered.append(current_string)
print(strings)
print(filtered)