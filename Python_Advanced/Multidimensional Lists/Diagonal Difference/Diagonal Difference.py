matrix = []


def create_matrix(count):
    for _ in range(count):
        r = list(map(lambda x: int(x), input().split()))
        matrix.append(r)
    return matrix, first_diagonal()


def first_diagonal():
    pos = 0
    sum_diagonal_1 = 0
    for i in range(len(matrix)):
        row = matrix[i]
        sum_diagonal_1 += row[pos]
        pos += 1
    return sec_diagonal(sum_diagonal_1)


def sec_diagonal(sum1):
    pos = 0
    sum_diagonal_2 = 0
    for i in range(len(matrix)-1, -1, -1):
        row = matrix[i]
        sum_diagonal_2 += row[pos]
        pos += 1
    return print_out(sum1, sum_diagonal_2)


def print_out(sum1, sum2):
    print(abs(sum1-sum2))


create_matrix(int(input()))
