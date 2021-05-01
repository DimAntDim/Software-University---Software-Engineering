def create_matrix(size):
    for _ in range(size):
        matrix.append(list(map(lambda x: int(x), input().split(', '))))
    return matrix


matrix = []
create_matrix(int(input()))
first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][(len(matrix)-1)-i] for i in range(len(matrix))]

print(f"First diagonal: {', '.join(map(lambda x: str(x), first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(map(lambda x: str(x), second_diagonal))}. Sum: {sum(second_diagonal)}")
