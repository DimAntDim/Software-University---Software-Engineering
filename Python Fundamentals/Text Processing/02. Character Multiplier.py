string = input().split(' ')
string1 = string[0]
string2 = string[1]
length1 = len(string1)
length2 = len(string2)

end = 0

if length1 > length2:
    end = length2
    plus = [x for x in string1[end:]]
else:
    end = length1
    plus = [x for x in string2[end:]]

result = 0
for i in range(0, end):
    result += ord(string1[i])*ord(string2[i])
to_be_add = 0
for i in plus:
    to_be_add += ord(i)

result += to_be_add
print(result)
