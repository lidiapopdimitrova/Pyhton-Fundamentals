def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    left_half = ticket[:10]
    right_half = ticket[10:]
    winning_chars = ["$", "@", "#", "^"]
    for winning_char in winning_chars:
        for repetition in range(10, 5, -1):
            char_repetition = winning_char * repetition
            if char_repetition in right_half and char_repetition in left_half:
                if repetition == 10:
                    return f'ticket "{ticket}" - {len(char_repetition)}{winning_char} Jackpot!'
                elif 6 <= repetition <= 9:
                    return f'ticket "{ticket}" - {len(char_repetition)}{winning_char}'
    return f'ticket "{ticket}" - no match'


tickets = [s.strip() for s in input().split(", ")]
ticket_state = []

for ticket in tickets:
    ticket_state.append(is_winning(ticket))
print("\n".join(ticket_state for ticket_state in ticket_state))