import re

cypher = input().split()
decipher_code = []
for w in cypher:
    decipher = ''
    number = re.search(r'\d+', w).group()
    decipher += chr(int(number))
    word_after_integer = w.replace(number, '')
    if len(word_after_integer) > 1:
        decipher += word_after_integer[-1]
        decipher += word_after_integer[1:-1]
        decipher += word_after_integer[0]
    else:
        decipher += word_after_integer[-1]
    decipher_code.append(decipher)
print(' '.join(decipher_code))
