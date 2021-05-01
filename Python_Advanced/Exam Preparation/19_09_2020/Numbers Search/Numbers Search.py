def numbers_searching(*args):
    duplicates = []
    numbers = list(args)
    missing_number = int
    for num in numbers:
        if numbers.count(num) > 1:
            if num not in duplicates:
                duplicates.append(num)
    numbers = sorted(numbers)
    duplicates = sorted(duplicates)
    for i in range(numbers[0], numbers[-1]+1):
        if i not in duplicates and numbers[0] < i < numbers[-1]:
            missing_number = i
            break
    result = [missing_number, sorted(duplicates)]
    return result


print(numbers_searching(2, 2, 4, 2, 6, 3, 5, 4, 6, 8, 8))
print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49,  48, 44, 48))
