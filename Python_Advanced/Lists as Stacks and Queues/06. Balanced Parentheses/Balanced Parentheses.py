from collections import deque
q = deque()
data = input()
flag = False
for ch in data:
    q.append(ch)
variant_A = '{}'
variant_B = '[]'
variant_C = '()'
variant_D = ''
while q:
    match_1 = q.popleft()
    match_2 = q.pop()
    pattern = match_1+match_2
    if pattern == variant_A or pattern == variant_B or pattern == variant_C or pattern == variant_D:
        flag = True
    else:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
