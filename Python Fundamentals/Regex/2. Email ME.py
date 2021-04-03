# mail = input().split('@')
# sum1 = 0
# sum2 = 0
# for i in mail[0]:
#     sum1 += ord(i)
# for i in mail[1]:
#     sum2 += ord(i)
#
# result = sum1 - sum2
# if result >= 0:
#     print('Call her!')
# else:
#     print("She is not the one.")
import re
mail = input()
pattern = r'([\w+\d+\_\.\-]+)@([\w+\d+\_\.\-]+)'
match = re.findall(pattern, mail)
sum1 = 0
sum2 = 0
for i in mail[0]:
    sum1 += ord(i)
for i in mail[1]:
    sum2 += ord(i)
if sum1-sum2 >= 0:
    print('Call her!')
else:
    print('She is not the one.')