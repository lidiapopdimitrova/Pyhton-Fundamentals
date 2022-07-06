cards_input = input().split()
number_of_shuffles = int(input())
length = len(cards_input)
half_size = int(length / 2)


for _ in range(0, number_of_shuffles):
    list_cards = []
    for p in range(0, half_size):
        list_cards.append(cards_input[p])
        list_cards.append(cards_input[half_size])
        half_size += 1
    cards_input = list_cards
    half_size = int(length / 2)
print(list_cards)

