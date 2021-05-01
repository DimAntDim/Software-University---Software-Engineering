
def create_matrix(count, columns):
    matrix = []
    for _ in range(count):
        row = input().split(' ')
        matrix.append(row)
    return manipulation(matrix, columns, count)


def manipulation(matrix, col, rows):
    while True:
        command = input().split(' ')
        if command[0] == 'END':
            break
        if command[0] != 'swap' or len(command) != 5:
            print('Invalid input!')
        else:
            row1 = int(command[1])
            col1 = int(command[2])
            row2 = int(command[3])
            col2 = int(command[4])
            if 0 <= row1 < rows and 0 <= row1 < rows and 0 <= col1 < col and 0 <= col1 < col:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for _ in matrix:
                    print(' '.join(_))
            else:
                print('Invalid input!')


n = input().split(' ')
create_matrix(int(n[0]), int(n[1]))
