data = input().split()
words = {}
for d in data:
    d_lower = d.lower()
    if d_lower not in words:
        words[d_lower] = 0
    words[d_lower] += 1

for (key, value) in words.items():
    if value % 2 != 0:
        print(key, end=' ')
