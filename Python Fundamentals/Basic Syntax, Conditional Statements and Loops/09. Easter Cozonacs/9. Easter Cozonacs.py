budget = float(input())
flour = float(input())

eggs = flour*0.75
milk = flour+0.25*flour

cozonac = eggs+flour+milk*0.25

cozonac_counter = 0
colored_eggs = 0

while True:

    if budget < cozonac:
        break
    cozonac_counter += 1
    colored_eggs += 3
    budget -= cozonac

    if cozonac_counter % 3 == 0:
        colored_eggs -= cozonac_counter-2
price = cozonac*cozonac_counter
print(f"You made {cozonac_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

"""
Since it’s Easter you have decided to make some cozonacs and exchange them for eggs.
Create a program that calculates how much cozonacs you can make with the budget you have. First, 
you will receive your budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one cozonac:
Eggs
1 pack
Flour
1 kg
Milk
0.250 l
The price for 1 pack of eggs is 75% of the price for 1 kg flour. 
The price for 1l milk is 25% more than price for 1 kg flour. Notice, 
that you need 0.250l milk for one cozonac and the calculated price is for 1l.
Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
For every cozonac that you make, you will receive 3 colored eggs. 
For every 3rd cozonac that you make, you will lose some of your colored eggs after you have 
received the usual 3 colored eggs for your cozonac. The count of eggs you will lose is calculated 
when you subtract 2 from your current count of cozonacs – ({currentCozonacsCount} – 2)
In the end, print the cozonacs you made, the eggs you have gathered and the money you have left, 
formatted to the 2nd decimal place, in the following format:
"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."
Input / Constraints
On the 1st line you will receive the budget – a real number in the range_shot [0.0…100000.0]
On the 2nd line you will receive the price for 1 kg flour – a real number in the range_shot [0.0…100000.0]
The input will always be in the right format.
You will always have a remaining budget.
There will not be a case in which the eggs become a negative count.
Output
In the end print the count of cozonacs you have made, the colored eggs you have gathered and the money 

formatted to the 2nd decimal place in the format described above.
Examples
Input
Output
20.50
1.25
You made 7 cozonacs! Now you have 16 eggs and 2.45BGN left.
Comments
We start by calculating the price for a pack of eggs, which is 75% of the price for 1 kg floor, 
which in this case is 1.25. The pack of eggs price is 0.9375. The price for 1l milk is 25% more 
than the price for 1kg floor and in this case it is – 1.5625, but we need the price for 0.250ml, which is - 0.390625. 
The total price for one cozonac is:
1.25 + 0.9375 + 0.390625 = 2.578125.
And we start subtracting the price for a single cozonac from the budget, and for each cozonac we receive 3 eggs. 
So after the first subtraction we will have 17.921875 budget, 1 cozonac and 3 eggs. After the second - 15.34375 budget,
6 eggs, and on the third - 12.765625 budget and 9 eggs and since it’s the third, we need to subtract the lost eggs, 
which will be 3 – 2 = 1, so we subtract 1 from 9 and our eggs become 8. We continue subtracting money from the budget
until the money aren't enough for us to make a cozonac. In the end we have 2.45BGN left.

15.75
1.4
You made 5 cozonacs! Now you have 14 eggs and 1.31BGN left.
"""
