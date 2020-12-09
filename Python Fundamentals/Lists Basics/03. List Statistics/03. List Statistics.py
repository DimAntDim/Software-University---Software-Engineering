"""
You will be given a number total_electrons. On the next total_electrons lines you will receive integers. You have to create and print two lists:
One with all the positives (including 0) numbers
One with all the negatives numbers
Finally print the following message: "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"
"""

n = int(input())
positive = []
negative = []
for i in range(n):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print(f"{positive}\n{negative}")
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")

