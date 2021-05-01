def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]
    i = 1
    next_row = []
    while len(magic_triangle) < n:
        current_row = magic_triangle[i]

        next_row.append(current_row[0])
        for i in range(1, len(current_row)):

            next_row.append(current_row[i]+current_row[i-1])
        next_row.append(current_row[-1])

        magic_triangle.append(next_row)
        next_row = []
        i += 1
    return magic_triangle


get_magic_triangle(5)
