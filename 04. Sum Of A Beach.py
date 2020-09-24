"""
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
Examples
Input
Output
WAtErSlIde
1
GolDeNSanDyWateRyBeaChSuNN
3
gOfIshsunesunFiSh
4
cItYTowNcARShoW
0
5.
"""
word = input()
word = word.lower()
sun = word.count('sun')
water = word.count('water')
sand = word.count('sand')
fish = word.count('fish')
sum = sun+water+fish+sand
print(sum)




