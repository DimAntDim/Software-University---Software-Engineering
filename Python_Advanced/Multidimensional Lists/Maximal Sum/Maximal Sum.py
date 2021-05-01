def create_matrix(count, col):
    matrix = []

    for _ in range(count):
        add_row = (list(map(lambda x: int(x), input().split(' '))))
        matrix.append(add_row)
    return matrix_3x3(matrix, col)


def matrix_3x3(mrx, columns):
    little_matrix = []
    cub_sum = 0
    max_matrix = []
    max_sum = 0
    cub_rows_pos = len(mrx) - 3
    cub_col_pos = columns - 3
    start_pos = 0

    for i in range(0, cub_rows_pos+1):

        for col_n in range(cub_col_pos+1):
            little_matrix.clear()

            for starting_element in range(3):
                row = mrx[starting_element][start_pos:start_pos+3]
                little_matrix.append(row)
                cub_sum += sum(row)
            if cub_sum > max_sum:
                max_sum = cub_sum
                max_matrix = little_matrix.copy()
            cub_sum = 0
            start_pos += 1

        mrx.remove(mrx[0])
        start_pos = 0
    return print_out(max_sum, max_matrix)


def print_out(max_sum, max_matrix):
    print(f"Sum = {max_sum}")
    for i in max_matrix:
        print(' '.join(map(lambda x: str(x), i)))


data = input().split(' ')
create_matrix(int(data[0]), int(data[1]))
