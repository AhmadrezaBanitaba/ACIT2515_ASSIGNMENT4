from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from abstract_menu_item import AbstractMenuItem
from menu_item_stats import MenuItemStats
from food import Food
from drink import Drink
from datetime import datetime


class MenuItemManager:
  
    """ creates menu item manager """    
    def __init__(self, restaurant_name, db_name):

        self._restaurant_name = restaurant_name
        if db_name is None or db_name == "":
            raise ValueError("DB Name cannot be undefined")
        engine = create_engine("sqlite:///" + db_name)
        self._db_session = sessionmaker(bind=engine)


    def add_menu_item(self, menu_item):
        """adds a menu item to the menu list"""   
        if menu_item is None or not isinstance(menu_item, AbstractMenuItem):
            raise ValueError("Invalid Menu Item.")

        # self._next_available_id = self._next_available_id + 1
        # menu_item.set_id(self._next_available_id)
        
        # if self.menu_exist(id):
        #     raise ValueError("mene item with given id already exists.")

        session = self._db_session()        
        session.add(menu_item)
        session.commit()
        session.close()






    def remove_menu_item(self, id):
        """ removes menu item if it exists """

        if id is None or not isinstance(id, int):
            raise ValueError("Invalid id")
        session = self._db_session()

        menu_item = session.query(AbstractMenuItem).filter(AbstractMenuItem.id == id).first()
        if menu_item is None:
            session.close()
            raise ValueError("id does not exist.")

        session.delete(menu_item)
        session.commit()
        session.close()






    def menu_exist(self, id):
        """checks if item exists """
        if id is None or not isinstance(id, int):
            raise ValueError("Invalid id.")
        session = self._db_session()
        menu_item = session.query(AbstractMenuItem).filter(AbstractMenuItem.id == id).first()
        session.close()

        if menu_item is not None:
            return True
        return False



    def get_by_id(self, id):
        """ returns menu item by id """
        if id is None or not isinstance(id, int):
            raise ValueError("Invalid id.")
        
        session = self._db_session()
        menu_item = session.query(Food).filter(Food.id == id).first()

        if menu_item is None:
            menu_item = session.query(Drink).filter(Drink.id == id).first()
        
        session.close()

        return menu_item
    
    def get_all_by_type(self, item_type):
        session = self._db_session()
        menu = session.query(AbstractMenuItem).filter(AbstractMenuItem.type == item_type).all()

        menu_list = []

        for i in menu:
            menu_list.append(i.menu_item_name)

        return menu_list

    def get_all(self):
        """ returns all items """
        session = self._db_session()
        total = 0
        menu = session.query(AbstractMenuItem).all()
        menu_list =[]
        for i in menu:
            menu_list.append(i.menu_item_name)


        session.close()

        return menu_list


    def update(self, menu_item):
        """ updates menu item """

        session = self._db_session()
        update_menuitem = session.query(AbstractMenuItem).filter(AbstractMenuItem.id == menu_item.get_id()).first()

        if update_menuitem is None:
            raise ValueError("Menu item not matched")




    def get_menu_item_stats(self):

        """ gets menu item stats """
        total_num_menu_items = int(0)
        num_foods = int(0)
        num_drinks = int(0)
        avg_price_food= float(0)
        avg_price_drink = float(0)
        item_price= float(0)
        food_price_list = []
        drink_price_list = []

        session = self._db_session()
        menu =  session.query(AbstractMenuItem).all()
        session.close()


        for menu_item in menu:
            total_num_menu_items += 1
            if menu_item.type == "food":
                num_foods += 1
                item_price = menu_item.price
                food_price_list.append(item_price)
                avg_price_food = sum(food_price_list) / len(food_price_list)
            if menu_item.type == "drink":
                num_drinks += 1
                item_price = menu_item.price
                drink_price_list.append(item_price)
                avg_price_drink = sum(drink_price_list) / len(drink_price_list)

        stats = MenuItemStats(total_num_menu_items,num_foods, num_drinks, avg_price_food, avg_price_drink)

        return stats


    