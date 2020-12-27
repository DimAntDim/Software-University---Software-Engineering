num = int(input())

loading_bar = []


def loading(num):
    percent = num // 10
    rest = 10 - percent
    for p in range(percent):
        loading_bar.append('%')
    for i in range(rest):
        loading_bar.append('.')

    if num == 100:
        print(f"100% Complete!\n[{''.join(loading_bar)}]")
    else:
        print(f"{num}% [{''.join(loading_bar)}]\nStill loading...")


loading(num)
