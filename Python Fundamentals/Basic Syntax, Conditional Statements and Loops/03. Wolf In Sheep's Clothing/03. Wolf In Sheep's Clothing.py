list = input()
sheep_list = list.split(', ')
counter = 0
sheep_counter = []
list = []
len_of_sheep_list = len(sheep_list)-1
for i in sheep_list:
    if i == 'sheep':
        list.append(len_of_sheep_list)
        len_of_sheep_list -= 1
    else:
        list.append('wolf')
        w = list.count(i)

len_of_list = len(list)
for l in list:
    if l == 'wolf' and l == list[-1]:
        print("Please go away and stop eating my sheep")
        break
    if l == 'wolf':
        print(f"Oi! Sheep number {len_of_list-1}! You are about to be eaten by a wolf!")
    len_of_list -= 1