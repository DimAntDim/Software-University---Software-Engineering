data = input().split(', ')
result=[]

for i in data:
    flag = True
    if 3 <= len(i) <= 16:
        for c in i:
            if c.isdigit() or c.isalpha() or c == '-' or c == '_':
                pass
            else:
                flag = False
                break
        if flag:
            result.append(i)
for name in result:
    print(name)