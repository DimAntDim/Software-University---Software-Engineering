words = input().split()
count_strings = {}
for word in words:
    for w in word:
        if w not in count_strings:
            count_strings[w] = 0
        count_strings[w] += 1

for i in count_strings:
    print(f"{i} -> {count_strings[i]}")
