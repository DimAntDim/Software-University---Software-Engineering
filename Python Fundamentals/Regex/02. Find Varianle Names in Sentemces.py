# import re
# text = input()
#
# pattern = re.compile(r"\b_[a-zA-Z0-9]+\b")
# match = re.findall(pattern, text)
# result = []
# for i in match:
#     result.append(i[1:])
# print(','.join(result))

text = input().split()
result = []
for i in text:
    if i.startswith('_') and i.count('_')<2 and not i.endswith('_'):
        result.append(i.lstrip('_'))
print(','.join(result))