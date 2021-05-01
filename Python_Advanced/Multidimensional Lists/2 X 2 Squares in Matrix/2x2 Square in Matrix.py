
def create_matrix(count):
    matrix = []

    for _ in range(count):
        row = input().split(' ')
        matrix.append(row)
    return check(matrix)


def check(m):
    result = 0
    # for every row in matrix:
    for i in range(len(m)):
        row = m[i]
        # take first element from first row
        el_1 = row[0]

        # for every element from the row check if is the same like the one before
        for element in range(1, len(row)):
            el_2 = row[element]
            # if the tow elements are the same
            if el_1 == el_2:
                # take the indexes of the two elements
                pos_el_2 = element
                pos_el_1 = pos_el_2 - 1

                # take the index of the next row if the next row is in range of the matrix
                # and check if the elements on the pos1 and pos2 are the same
                row_index = i
                if row_index+1 in range(len(m)):
                    next_row = m[row_index+1]
                    # if the elements on the pos1 and pos2 are the same add to result += 1
                    if next_row[pos_el_1] == row[pos_el_1] and next_row[pos_el_2] == row[pos_el_2]:
                        result += 1
            # if the element are not the same el_1 become el_2 and ...
            else:
                el_1 = el_2
    return print(result)


n = input().split(' ')
create_matrix(int(n[0]))
