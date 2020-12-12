def smallest_number(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


f_num = int(input())
s_num = int(input())
t_num = int(input())

print(smallest_number(f_num,s_num,t_num))
