"""
You Will Receive Two Lines of Input: a List of Employee's Happiness As String with Numbers Separated by a
Single Space and a Happiness Improvement Factor (Single Number). Your Task is to Find Out If the Employees
Are Generally Happy in Their Office. To Do That You Have to Increase Their Happiness by Multiplying the
All the Employee's Happiness (the Numbers from the List) by the Factor, Filter the Employees Which Happiness is
Greater Than or Equal to the Average in the New List and Print the Result
There are two types of output:
If the half or more of the employees have happiness >= than the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
Input
Otherwise: "Score: {happy_count}/{total_count}. Employees are not happy!"
1 2 3 4 2 1
3
Output
Score 2/6. Employees are not happy!
Input
2 3 2 1 3 3
4
Output
Score: 3/6. Employees are happy!
"""

happiness = list(map(lambda x: int(x), input().split()))

factor = int(input())

h_ls = [x * factor for x in happiness]
counter_happiness = 0
avg_happiness = sum(h_ls)/len(h_ls)

for emp in h_ls:
    if emp >= avg_happiness:
        counter_happiness += 1
if counter_happiness >= len(h_ls)/2:
    print(f"Score: {counter_happiness}/{len(h_ls)}. Employees are happy!")
else:
    print(f"Score: {counter_happiness}/{len(h_ls)}. Employees are not happy!")
