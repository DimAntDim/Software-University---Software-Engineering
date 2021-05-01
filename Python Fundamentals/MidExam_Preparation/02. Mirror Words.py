import re
string = input()
mirror_string = re.split("@|@@|@|#|##|#\s*", string)

while '' in mirror_string:
    mirror_string.remove('')
mirror_list = []
counter = []
#----Counter of pairs----
for st in range(len(mirror_string)):
    word = mirror_string[st]
    reversed_word = word[::-1]
    word = word.lower()
    reversed_word = reversed_word.lower()
    if reversed_word in string and word in string and 2 < len(word) == len(reversed_word):
        counter.append(word)
        counter.append(reversed_word)
print(len(counter))

for st in range(len(mirror_string)):
    word = mirror_string[st]
    reversed_word = word[::-1]
    reversed_word = ''.join(reversed_word)
    if reversed_word in string and word in string and 2 < len(word) == len(reversed_word):
        mirror_list.append(word)
        mirror_string.append(reversed_word)

print(round(len(counter)/2))

new_ls = []
final_list = []
for i in range(0, len(mirror_list), 2):
    start = mirror_list[i]
    end = mirror_list[i+1]
    result = string[string.find(start) + len(start):string.rfind(end)]
    if len(result) > 1 and result == '@@' or result == '##':
        final_list.append(f"{start} <=> {end}")
if len(final_list) > 0:
    print(', '.join(final_list))
else:
    print('No mirror words!')