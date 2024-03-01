import json
from tkinter import Button, Entry, Label
from GUI_Shop.canvas import tk
from GUI_Shop.helpers import clean_screen
from GUI_Shop.products import render_products


def register(**user):
    user.update({'products': []})
    with open("db/users.txt", "a") as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open("db/username_password.txt", "a") as f:
        user_data = f"{user.get('username')}, {user.get('password')}"
        f.write(user_data)
        f.write('\n')


def login(username, password):
    with open("db/username_password.txt", "r") as file:
        data = file.readlines()
        for line in data:
            name, user_password = line[:-1].split(', ')
            if name == username and password == user_password:
                render_products()
                break
        else:
            render_login(errors=True)


def render_register():
    clean_screen()
    Label(text="Enter your username").grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=1, column=0)
    Label(text="Enter your password").grid(row=2, column=0)
    password = Entry(tk)
    password.grid(row=3, column=0)
    Label(text="Enter your name").grid(row=4, column=0)
    first_name = Entry(tk)
    first_name.grid(row=5, column=0)
    Label(text="Enter your last name").grid(row=6, column=0)
    last_name = Entry(tk)
    last_name.grid(row=7, column=0)
    Button(tk, text='Register', bg='blue', fg='white',
           command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(), last_name=last_name.get())).grid(row=8, column=0)
    Button(tk, text='Home menu', command=render_main_screen).grid(row=10, column=0)


def render_login(errors=None):
    clean_screen()
    Label(text="Enter username").grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=1, column=0)
    Label(text="Enter password").grid(row=2, column=0)
    password = Entry(tk, show='*')
    password.grid(row=3, column=0)
    Button(tk, text='Login', bg='blue', fg='white',
           command=lambda: login(username=username.get(), password=password.get())).grid(row=4, column=0)
    Button(tk, text='Home menu', command=render_main_screen).grid(row=6, column=0)
    # if errors:
    #     Label(text='Invalid username or password').grid(row=5, column=0)


def render_main_screen():
    clean_screen()
    Button(tk, text='Login', bg='blue', fg='white', command=render_login().grid(row=0, column=0)
    Button(tk, text='Register', bg='yellow', command=render_register).grid(row=0, column=1)
