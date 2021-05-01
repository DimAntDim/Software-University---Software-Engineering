books = input().split('&')

command_line = input()


def add_book(book_name):
    if book_name not in books:
        books.insert(0, book_name)


def take_book(book_name):
    if book_name in books:
        books.remove(book_name)


def swap_book(book1, book2):
    book1_index = books.index(book1)
    book2_index = books.index(book2)
    books[book1_index] = book2
    books[book2_index] = book1


def insert_book(book):
    books.append(book)


while command_line != 'Done':
    data = command_line.split(' | ')
    command = data[0]
    if command == 'Add Book':
        book = data[1]
        add_book(book)
    elif command == 'Take Book':
        book = data[1]
        take_book(book)
    elif command == 'Swap Books':
        book_1 = data[1]
        book_2 = data[2]
        swap_book(book_1, book_2)
    elif command == 'Insert Book':
        book = data[1]
        insert_book(book)
    elif command == 'Check Book':
        index = int(data[1])
        if index < len(books):
            print(books[index])
    command_line = input()

print(', '.join(books))

