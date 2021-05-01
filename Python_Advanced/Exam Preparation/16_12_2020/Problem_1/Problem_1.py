from collections import deque


def pair_match(m, f):
    while m and f:
        next_male = m[-1]
        next_female = f[0]
        if next_female <= 0:
            f.popleft()
        elif next_male <= 0:
            m.pop()
        elif next_female == next_male:
            m.pop()
            f.popleft()
            total_match[0] += 1
        else:
            f.popleft()
            m[-1] -= 2
            if m[-1] <= 0:
                m.pop()

    return males, females, total_match


total_match = [0]
males = deque(list(map(int, input().split())))
females = deque(list(map(int, input().split())))
pair_match(males, females)

print(f"Matches: {total_match[0]}")
if males:
    males = list(map(str, males))
    ml = males[::-1]
    print(f"Males left: {', '.join(ml)}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
