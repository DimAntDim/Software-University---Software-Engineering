numbers = list(map(lambda x: int(x), input().split()))

avg = sum(numbers)/len(numbers)

top_5 = []
if len(numbers) > 4:
    for n in numbers:
        if n > avg:
            top_5.append(n)

    top_5.sort(reverse=True)
    list_to_print = list(map(lambda x: str(x), top_5))
    if len(top_5) < 5:
        print(' '.join(list_to_print))
    else:
        print(' '.join(list_to_print[:5]))
else:
    print('No')
