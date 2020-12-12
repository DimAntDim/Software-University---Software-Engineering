def add_and_subtract(a,b,c):
    def sum_numbers():
        result = a + b
        return result

    def subtract():
        return sum_numbers() - c

    return subtract()


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a,b,c))

