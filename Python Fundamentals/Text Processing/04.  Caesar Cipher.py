text = input().strip()
encripted = ''
for i in text:
    char = ord(i)+3
    encripted += chr(char)
print(encripted)