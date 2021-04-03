import re

n = int(input())

pattern = r"@(?P<planet>[A-Z][a-z]+).*?:(?P<population>\d+).*?[^!@\-\>\:]!(?P<attack>[A|D])!.*?->(?P<soldier>\d+).*"

enigma_letters = ['s', 't', 'a', 'r']
data_list = []
result = {'Attacked planets': [],
          'Destroyed planets': []
          }


def decrypter(code):
    decrypter_counter = 0
    decrypted = ''
    for w in code:
        if w.lower() in enigma_letters:
            decrypter_counter += 1
    for char in code:
        changed_char = ord(char) - decrypter_counter
        decrypted += chr(changed_char)
    return regex(decrypted)


def regex(decrypted):
    matches = re.finditer(pattern, decrypted)
    data = {}
    for match in matches:
        data = match.groupdict()
    if data:
        data_list.append(data)
    return data_list


def filter(datas):
    for i in datas:
        planet = i['planet']
        attack = i['attack']
        if attack == 'A':
            result['Attacked planets'].append(planet)
        else:
            result['Destroyed planets'].append(planet)
    return result


def print_out(result):
    for type_attack, planets in result.items():
        print(f"{type_attack}: {len(planets)}")
        for planet in sorted(planets):
            print(f"-> {planet}")


for i in range(n):
    code = input()
    decrypter(code)

filter(data_list)
print_out(result)
