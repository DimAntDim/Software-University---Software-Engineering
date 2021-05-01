n = int(input())
s = []
for i in range(n):
    data = input().split()
    command = data[0]
    if command == '1':
        num = data[1]
        s.append(int(num))
    elif command == '2':
        if len(s) > 0:
            s.pop()
    elif command == '3':
        max_n = 0
        for _ in s:
            if _ > max_n:
                max_n = _
        print(max_n)
    elif command == '4':
        min_n = s[0]
        for _ in range(1, len(s)):
            m = s[_]
            if min_n > m:
                min_n = m
        print(min_n)
s = s[::-1]
s = map(lambda x: str(x), s)

print(', '.join(s))
