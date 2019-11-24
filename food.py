from abstract_menu_item import AbstractMenuItem
from sqlalchemy import Column, String, Integer, Float, DateTime


class Food(AbstractMenuItem):
    """ creates food """

    cuisine_country = Column(String(100))
    main_ingredient = Column(String(20))
    portion_size = Column(String(20))
    is_vegetarian = Column(Integer)

    def __init__(self, menu_item_name, menu_item_no, date_added, price, calories, cuisine_country, main_ingredient, portion_size, is_vegetarian):
        super().__init__( menu_item_name, menu_item_no, date_added, price, calories)
        self._cuisine_country= cuisine_country
        self._main_ingredient= main_ingredient
        self._portion_size= portion_size
        self._is_vegetarian= is_vegetarian



    def to_dict(self):
        """Returns a dictionary representation of menu item of type food"""
        item_dict = {
            "id": self.get_id(),
            "menu_item_name": self._menu_item_name,
            "menu_item_no": self._menu_item_no,
            "date_added": self._date_added.strftime("%Y-%m-%d"),
            "price": self._price,
            "calories": self._calories,
            "cuisine_country": self._cuisine_country,
            "main_ingredient": self._main_ingredient,
            "portion_size": self._portion_size,
            "is_vegetarian": self._is_vegetarian,
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
        MENU_ITEM_TYPE = "food" 
        return MENU_ITEM_TYPE
        
    def get_portion_size(self):
        """ returns portion size """
        return self._portion_size

    def get_main_ingredient(self):
        """ returns main ingredient """
        return self._main_ingredient

    def get_cuisine_country(self):
        """ returns country of origin """
        return self._cuisine_country
    