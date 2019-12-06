
class MenuItemStats():
    """ Statistics on a Restaurant Menu """
    def __init__(self, total_num_menu_items , num_foods, num_drinks, avg_price_food, avg_price_drink):
        """ Initialize the data values """

        self._total_num_menu_items = total_num_menu_items
        self._num_foods = num_foods
        self._num_drinks = num_drinks
        self._avg_price_food = avg_price_food
        self._avg_price_drink = avg_price_drink




    def to_dict(self):
        """Returns a dictionary representation of repair shop stas"""
        menu_dict = {
            "_total_num_menu_items": self.get_total_num_menu_items(),
            "_num_foods": self.get_num_foods(),
            "_num_drinks": self.get_num_drinks(),
            "_avg_price_food": self.get_avg_price_food(),
            "_avg_price_drink": self.get_avg_price_drink()
        }
        return menu_dict


    def get_total_num_menu_items(self):
        """ returns  total number of menu  items """
        return self._total_num_menu_items

    def get_num_foods(self):
        """ returns total number of foods  """
        return self._num_foods

    def get_num_drinks(self):
        """ returns total number of drinks  """
        return self._num_drinks

    def get_avg_price_food(self):
        """ returns average price of food  """
        return self._avg_price_food

    def get_avg_price_drink(self):
        """ returns average price of drink  """
        return self._avg_price_drink
    