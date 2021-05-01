data = input().split("\\")
file = data[-1]
file = file.split('.')
print(f'File name: {file[0]}')
print(f"File extension: {file[1]}")