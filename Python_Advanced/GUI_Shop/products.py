import json
from tkinter import Button, Label
import os
from PIL import ImageTk, Image
from GUI_Shop.helpers import clean_screen
from GUI_Shop.canvas import tk

base_folder = os.path.dirname(__file__)


def render_products():
    clean_screen()
    with open("db/products.txt", "r") as file:
        products = file.readlines()
        column_counter = 0
        for product in products:
            current_product = json.loads(product)
            Label(text=current_product.get('name')).grid(row=0, column=0+column_counter)
            image = Image.open(os.path.join(base_folder, "images"), current_product.get('img_path'))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=1, column_counter=0+column_counter)
            Button(tk, text=f"Buy {current_product.get('id')}").grid(row=3, column=0+column_counter)
            column_counter += 1
