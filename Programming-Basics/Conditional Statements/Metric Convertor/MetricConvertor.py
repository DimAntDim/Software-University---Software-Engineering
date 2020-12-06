number = float(input())

metric = input("")
metric1 = input("")

output = 0
if metric == 'm' and metric1 == 'mm':
    output = number * 1000
elif metric == 'm' and metric1 == 'cm':
    output = number * 100
elif metric == 'cm' and metric1 == 'mm':
    output = number * 10
elif metric == 'cm' and metric1 == 'm':
    output = number / 100
elif metric == 'mm' and metric1 == 'cm':
    output = number / 10
elif metric == 'mm' and metric1 == 'm':
    output = number / 1000

print("%.3f" % output)