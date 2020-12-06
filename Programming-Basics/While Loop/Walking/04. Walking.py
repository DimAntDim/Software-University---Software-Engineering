goal = 10000
step_counter = 0
while True:
    steps = input()
    if steps == 'Going home':
        last_steps = int(input())
        step_counter += last_steps
        if step_counter == goal:
            print("Goal reached! Good job!")
        elif step_counter > goal:
            print("Goal reached! Good job!")
            print(f"{step_counter - goal} steps over the goal!")
        else:
            print(f"{goal - step_counter} more steps to reach goal.")
        break
    steps = int(steps)
    step_counter += steps
    if step_counter == goal:
        print("Goal reached! Good job!")
        break
    elif step_counter > goal:
        print("Goal reached! Good job!")
        print(f"{step_counter-goal} steps over the goal!")
        break