goal = 10000
goal_reached = False
command = input()
step_counter = 0
while command != 'Going home':
    steps = int(command)
    step_counter += steps
    if step_counter >= goal:
        goal_reached = True
        break
    command = input()
else:
    last_steps_for_the_day = int(input())
    step_counter += last_steps_for_the_day
    if step_counter >= goal:
        goal_reached = True

diff = abs(goal - step_counter)
if goal_reached:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

