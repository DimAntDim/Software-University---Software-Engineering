nums = list(map(int, input().split()))
negative_nums = [x for x in nums if x < 0]
positive_nums = [x for x in nums if x > 0]

print(sum(negative_nums))
print(sum(positive_nums))
if abs(sum(negative_nums)) > abs(sum(positive_nums)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
