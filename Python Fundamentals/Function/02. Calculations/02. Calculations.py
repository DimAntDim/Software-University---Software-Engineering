operator_command = input()
x = int(input())
y = int(input())


def calculator(operator, n1, n2):
    if operator == 'subtract':
        return n1-n2
    elif operator == 'add':
        return n1+n2
    elif operator == 'divide':
        return round(n1/n2)
    elif operator == 'multiply':
        return n1*n2


print(calculator(operator_command, x, y))