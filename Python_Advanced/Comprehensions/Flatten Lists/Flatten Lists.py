data = input().split('|')
print(*[' '.join([el for el in element if el != ' ']) for element in data[::-1]], sep=' ')
