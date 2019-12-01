import tkinter as tk
import requests
from add_food_popup import AddFoodPopup
from add_drink_popup import AddDrinkPopup
from remove_menu_item_popup import RemoveMenuItemPopup

class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Menu Items").grid(row=1, column=2)
        self._menu_items_listbox = tk.Listbox(self, width= 120)
        self._menu_items_listbox.grid(row=2, column=1, columnspan=5)

        tk.Button(self, text="Add Food", command=self._add_food).grid(row=3, column=1)
        tk.Button(self, text="Add Drink", command=self._add_drink).grid(row=3, column=2)
        tk.Button(self, text="Remove Menu Item", command=self._remove_menu_item,  fg="red").grid(row=3, column=3)
        tk.Button(self, text="Quit", command=self._quit_callback).grid(row=4, column=2)

        self._update_menu_items_list()
        self._menu_item_stats()

    def _add_food(self):
        """ Add Food Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddFoodPopup(self._popup_win, self._close_food_cb)

    def _close_food_cb(self):
        """ Close Add Food Popup """
        self._popup_win.destroy()
        self._update_menu_items_list()
        self._menu_item_stats()

    def _remove_menu_item(self):
        """ Remove Menu Item Popup """
        self._popup_win = tk.Toplevel()
        self._popup = RemoveMenuItemPopup(self._popup_win, self._close_menu_item_cb)

    def _close_menu_item_cb(self):
        """ Close Remove Item Popup """
        self._popup_win.destroy()
        self._update_menu_items_list()
        self._menu_item_stats()


    def _add_drink(self):
        """ Add Tablet Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddDrinkPopup(self._popup_win, self._close_drink_cb)


    def _close_drink_cb(self):
        """ Close Add Tablet Popup """
        self._popup_win.destroy()
        self._update_menu_items_list()
        self._menu_item_stats()



    def _quit_callback(self):
        """ Quit """
        self.quit()

    def _update_menu_items_list(self):
        """ Update the List of Menu Items Descriptions """
        response = requests.get("http://127.0.0.1:5000/menu/menu_items/all/food")
        response_drink = requests.get("http://127.0.0.1:5000/menu/menu_items/all/drink")

        if response.status_code == 200:
            food_descs = response.json()
            self._menu_items_listbox.delete(0, tk.END)
            for food_desc in food_descs:
                self._menu_items_listbox.insert(tk.END, food_desc)

        if response_drink.status_code == 200:
            drink_descs = response_drink.json()
            for drink_desc in drink_descs:
                self._menu_items_listbox.insert(tk.END, drink_desc)



    def _menu_item_stats(self):
        """ Repair Statistics """
        response = requests.get("http://127.0.0.1:5000/menu/menu_items/stats")

        if response.status_code == 200:
            menu_items_stats = response.json()
            self._menu_items_listbox.insert(tk.END, menu_items_stats)





   
if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

