"""
You will receive a todo-notes until you get the data "End". The notes will be in the format: "{importance}-{value}".
Return the list of todo-notes sorted by importance. The maximum importance will be 10
Input
Output
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End
['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
"""
task_ls = ['0']*10


def task_org(i, t):
    task_ls.insert(i, t)
    task_ls.pop(i+1)
    return task_ls


while True:
    task_input = input().split('-')
    if task_input[0] == 'End':
        break
    importance = int(task_input[0])-1
    task = task_input[1]
    task_org(importance, task)

while '0' in task_ls:
    task_ls.remove('.')

print(task_ls)