def snake_matrix(string, rows, cols):
    matrix = []
    char_index = 0
    line = ''
    char = 0
    counter = 0
    while counter < rows*cols:
        if len(line) == rows * cols:
            break

        if char == len(string):
            char = 0
        else:
            line += string[char]
            char += 1

    for i in range(rows):
        row = line[0:cols]
        if i % 2 == 0:
            matrix.append(row)
        else:
            matrix.append(row[::-1])
        line = line.replace(row, '', 1)

    for r in matrix:
        print(r)


m = input().split(' ')
string_input = input()
snake_matrix(string_input, int(m[0]), int(m[1]))
