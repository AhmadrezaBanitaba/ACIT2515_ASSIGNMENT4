from abstract_menu_item import AbstractMenuItem
from sqlalchemy import Column, String, Integer, Float, DateTime


class Food(AbstractMenuItem):
    """ creates food """
    MENU_ITEM_TYPE = "food"
    cuisine_country = Column(String(100))
    main_ingredient = Column(String(20))
    portion_size = Column(String(20))
    is_vegetarian = Column(Integer)

    def __init__(self, menu_item_name, menu_item_no, date_added, price, calories, cuisine_country, main_ingredient, portion_size, is_vegetarian):
        super().__init__( menu_item_name, menu_item_no, date_added, price, calories, Food.MENU_ITEM_TYPE)
        self.cuisine_country= cuisine_country
        self.main_ingredient= main_ingredient
        self.portion_size= portion_size
        self.is_vegetarian= is_vegetarian




    def to_dict(self):
        """Returns a dictionary representation of menu item of type food"""
        item_dict = {
            "menu_item_name": self.menu_item_name,
            "menu_item_no": self.menu_item_no,
            "date_added": self.date_added.strftime("%Y-%m-%d"),
            "price": self.price,
            "calories": self.calories,
            "cuisine_country": self.cuisine_country,
            "main_ingredient": self.main_ingredient,
            "portion_size": self.portion_size,
            "is_vegetarian": self.is_vegetarian,
            "type": self.get_type()
        }
        return item_dict



    def menu_item_description(self):
        """ prints description """
        if self._is_vegetarian is True:
            return "Food item ""%s"" with menu index of %s added on %s with the price of %s, containing %s calories has a country origin of %s and its main ingredient is %s . Portion size is %s and the food is vegetarian" % (self._menu_item_name, self._menu_item_no,self._date_added, self._price, self._calories, self._cuisine_country, self._main_ingredient, self._portion_size)  
        else:
            return "Food item ""%s"" with menu index of %s added on %s with the price of %s, containing %s calories has a country origin of %s and its main ingredient is %s . Portion size is %s and the food is non vegetarian" % (self._menu_item_name, self._menu_item_no,self._date_added, self._price, self._calories, self._cuisine_country, self._main_ingredient, self._portion_size)
    
    def get_type(self):
        """ returns menu item type """
        return Food.MENU_ITEM_TYPE

    def get_portion_size(self):
        """ returns portion size """
        return self.portion_size

    def get_main_ingredient(self):
        """ returns main ingredient """
        return self.main_ingredient

    def get_cuisine_country(self):
        """ returns country of origin """
        return self.cuisine_country
    