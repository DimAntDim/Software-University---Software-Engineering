ls = []
def character_in_range(ch1, ch2):
    for c in range(ord(ch1)+1, ord(ch2)):
        ls.append(chr(c))

a = input()
b = input()

character_in_range(a,b)
print(' '.join(ls))