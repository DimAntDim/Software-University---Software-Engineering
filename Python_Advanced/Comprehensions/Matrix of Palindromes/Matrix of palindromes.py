def palindrome_matrix(rows, cols):
    matrix = []
    for r in range(97, 97 + rows):
        row = [f"{chr(r)}{chr(r+c)}{chr(r)}" for c in range(cols)]
        matrix.append(row)

    return matrix_print(matrix)


def matrix_print(m):
    print(*[' '.join(el) for el in m], sep='\n')


parameters = input().split()
row_n = int(parameters[0])
cols_n = int(parameters[1])
palindrome_matrix(row_n, cols_n)
