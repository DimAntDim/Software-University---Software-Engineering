movie = input()

days = int(input())
tickets = int(input())
price = float(input())
total = days * tickets * price

cinema_profit = float(input())*total/100

print(f"The profit from the movie {movie} is {total - cinema_profit:.2f} lv.")