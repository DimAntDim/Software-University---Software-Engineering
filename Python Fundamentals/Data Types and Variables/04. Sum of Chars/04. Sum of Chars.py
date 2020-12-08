"""
Write a program, which sums the ASCII codes of total_electrons characters and prints the sum on the console.
Input
On the first line, you will receive total_electrons – the number of lines, which will follow
On the next total_electrons lines – you will receive letters from the Latin alphabet
Output
Print the total sum in the following format:
The sum equals: {total_sum}
Constraints
total_electrons will be in the interval [1…20].
The characters will always be either upper or lower-case letters from the English alphabet
You will always receive one letter per line
"""
n = int(input())
sum = 0
for i in range(n):
    l = input()
    sum += ord(l)
print(f"The sum equals: {sum}")
