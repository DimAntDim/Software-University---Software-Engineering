import os
try:
    os.remove("../Fle Writer/my_first_file.txt")
except FileNotFoundError:
    print('File already deleted!')
