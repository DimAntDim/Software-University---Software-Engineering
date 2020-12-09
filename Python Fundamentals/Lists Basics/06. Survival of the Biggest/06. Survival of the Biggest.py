import heapq
inp = input().split()
n = int(input())
new_list = []
elements_for_remove = []
# Create new list base on list with name l and integer value of the elements
for i in inp:
    new_list.append(int(i))
# Searching the total_electrons smallest elements and put them in new_list
elements_for_remove = heapq.nsmallest(n, new_list)
# remove the smallest elements from new_list
for element in elements_for_remove:
    if element in new_list:
        new_list.remove(element)
print(new_list)

