tickets = int(input())
budget = int(input())
price_for_ticket = int(input())

total_price = tickets*price_for_ticket

if budget >= total_price:
    print(f"You can sell your client {tickets} tickets for the price of {total_price}$!")
    print(f"Your client should become a change of {budget - total_price}$!")
else:
    print(f"The budget of {budget}$ is not enough. Your client can't buy {tickets} tickets with this budget!")