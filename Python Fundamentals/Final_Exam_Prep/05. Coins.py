import math
insert = float(input())*100
coin_counter = 0
first_coin = math.floor(insert/100)
second_coin = insert % 100
tird_coin = int(insert % 10)
second_coin = int(math.floor(second_coin - tird_coin)/10)
coin_20st = 0
coin_10st = 0
coin_2st = 0
coin_1st = 0

coin_2lv = first_coin // 2
coin_counter += coin_2lv
#print(f"Монети от 2 лв.: {coin_2lv} бр.")
coin_1lv = first_coin - coin_2lv*2
#print(f"Монети от 1 лв.: {coin_1lv} бр.")

coin_50st = second_coin // 5
if coin_50st > 0:
  #  print(f"Монети от 50 ст. {coin_50st} бр.")
    second_coin -= coin_50st*5
    coin_20st = second_coin // 2
  #  print(f"Монети от 20 ст. {coin_20st} бр.")
    second_coin -= coin_20st*2
    coin_10st = second_coin
  #  print(f"Монети от 10 ст. {coin_10st} бр.")
elif coin_50st < 0:
    coin_20st = second_coin // 2
  #  print(f"Монети от 20 ст. {coin_20st} бр.")
    second_coin -= coin_20st * 2
    coin_10st = second_coin
 #   print(f"Монети от 10 ст. {coin_10st} бр.")


coin_5st = tird_coin // 5
if coin_5st > 0:
  #  print(f"Монети от 5 ст. {coin_5st} бр.")
    tird_coin -= coin_5st*5
    coin_2st = tird_coin // 2
 #   print(f"Монети от 2 ст. {coin_2st} бр.")
    tird_coin -= coin_2st*2
    coin_1st = tird_coin
 #   print(f"Монети от 1 ст. {coin_1st} бр.")
elif coin_5st == 0:
    coin_2st = tird_coin // 2
  #  print(f"Монети от 2 ст. {coin_2st} бр.")
    tird_coin -= coin_2st * 2
    coin_1st = tird_coin
  #  print(f"Монети от 1 ст. {coin_1st} бр.")


coin_counter = coin_2lv+coin_1lv+coin_50st+coin_20st+coin_10st+coin_5st+coin_2st+coin_1st
print(coin_counter)