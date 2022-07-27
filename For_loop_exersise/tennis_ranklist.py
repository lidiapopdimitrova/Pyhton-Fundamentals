import math

tournaments = int(input())
starting_points = int(input())
wins = 0
points = 0

for i in range(tournaments):
    result = input()
    if result == "F":
        points += 1200

    elif result == "W":
        points += 2000
        wins += 1
    elif result == "SF":
        points += 720

average_points = points // tournaments
points += starting_points
percent_wins = wins / tournaments * 100
down = math.floor(average_points)

print(f"Final points: {points}")
print(f"Average points: {down}")
print(f"{percent_wins:.2f}%")






