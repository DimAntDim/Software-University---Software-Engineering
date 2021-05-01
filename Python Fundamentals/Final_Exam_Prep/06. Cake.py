cake_size_x = int(input())
cake_size_y = int(input())
cake = cake_size_x*cake_size_y
pieces = 0
while True:
    piece = input()
    if piece == 'STOP':
        pieces_left = cake - pieces
        print(f"{pieces_left} pieces are left.")
        break
    piece = int(piece)
    pieces += piece
    if pieces >= cake:
        print(f"No more cake left! You need {abs(cake-pieces)} pieces more.")
        break

    print(pieces)
