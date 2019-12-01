import tkinter as tk
from tkinter import messagebox
import requests
import re


class AddDrinkPopup(tk.Frame):
    """ Popup Frame to Add drink """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Menu Item Name").grid(row=1, column=1)
        self._menu_item_name = tk.Entry(self)
        self._menu_item_name.grid(row=1, column=2)
        tk.Label(self, text="menu item no:").grid(row=2, column=1)
        self._menu_item_no = tk.Entry(self)
        self._menu_item_no.grid(row=2, column=2)
        tk.Label(self, text="date added:").grid(row=3, column=1)
        self._date_added = tk.Entry(self)
        self._date_added.grid(row=3, column=2)
        tk.Label(self, text="price: ").grid(row=4, column=1)
        self._price = tk.Entry(self)
        self._price.grid(row=4, column=2)
        tk.Label(self, text="calories:").grid(row=5, column=1)
        self._calories = tk.Entry(self)
        self._calories.grid(row=5, column=2)
        tk.Label(self, text="manufacturer:").grid(row=6, column=1)
        self._manufacturer = tk.Entry(self)
        self._manufacturer.grid(row=6, column=2)
        tk.Label(self, text="size:").grid(row=7, column=1)
        self._size = tk.Entry(self)
        self._size.grid(row=7, column=2)
        tk.Label(self, text="is fizzy:").grid(row=8, column=1)
        self._is_fizzy = tk.Entry(self)
        self._is_fizzy.grid(row=8, column=2)
        tk.Label(self, text="is hot:").grid(row=9, column=1)
        self._is_hot = tk.Entry(self)
        self._is_hot.grid(row=9, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=10, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=10, column=2)

    def _submit_cb(self):
        """ Submit the Add drink """

        # Validate the non-string data values
        if re.match("^\d{4}-\d{2}-\d{2}$", self._date_added.get()) is None:
            messagebox.showerror("Error", "Date added must have format yyyy-mm-dd")
            return

        if re.match("^\d+$", self._calories.get()) is None:
            messagebox.showerror("Error", "calories must be a valid integer")
            return


        if re.match("^\d+.\d{2}$", self._price.get()) is None:
            messagebox.showerror("Error", "Price must be a valid price")
            return

        # Create the dictionary for the JSON request body
        data = {}
        data['menu_item_name'] = self._menu_item_name.get()
        data['menu_item_no'] = self._menu_item_no.get()
        data['date_added'] = self._date_added.get()
        data['price'] = float(self._price.get())
        data['calories'] = int(self._calories.get())
        data['manufacturer'] = self._manufacturer.get()
        data['size'] = self._size.get()
        data['is_fizzy'] = bool(self._is_fizzy.get())
        data['is_hot'] = bool(self._is_hot.get())
        data['type'] = "drink"

        # Implement your code here
        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/menu/menu_items", json=data, headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Add phone request failed " + response.text)

