from abstract_menu_item import AbstractMenuItem
from sqlalchemy import Column, String, Integer, Float, DateTime


class Drink(AbstractMenuItem):
    """ creates drink """

    MENU_ITEM_TYPE = "drink"
    manufacturer = Column(String(100))
    size = Column(String(20))
    is_fizzy = Column(Integer)
    is_hot = Column(Integer)

    def __init__(self, menu_item_name, menu_item_no, date_added, price, calories, manufacturer, size, is_fizzy, is_hot):
        super().__init__( menu_item_name, menu_item_no, date_added, price, calories, Drink.MENU_ITEM_TYPE)
        self.manufacturer= manufacturer
        self.size= size
        self.is_fizzy= is_fizzy
        self.is_hot= is_hot


    def to_dict(self):
        """Returns a dictionary representation of menu item of type food"""
        item_dict = {
            "menu_item_name": self.menu_item_name,
            "menu_item_no": self.menu_item_no,
            "date_added": self.date_added.strftime("%Y-%m-%d"),
            "price": self.price,
            "calories": self.calories,
            "manufacturer": self.manufacturer,
            "size": self.size,
            "is_fizzy": self.is_fizzy,
            "is_hot": self.is_hot,
            "type": self.get_type()
        }
        return item_dict

    def menu_item_description(self):
        if self._is_fizzy is True:
            return "%s is a fizzy drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size) 
        elif self._is_fizzy is False:
            return "%s is a non-fizzy drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size)
        elif self._is_hot is True:
            return "%s is a hot drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size)
        elif self._is_hot is False:
            return "%s is a cold drink item with menu index %s added on %s with the price of %s, containing %s calories made by %s and is %s ml " % (self._menu_item_name, self._menu_item_no, self._date_added, self._price, self._calories, self._manufacturer, self._size)
    
    def get_type(self):
        """ returns menu item type """
        return Drink.MENU_ITEM_TYPE


    def get_manufacturer(self):
        return self.manufacturer

    def get_size(self):
        return self.size



