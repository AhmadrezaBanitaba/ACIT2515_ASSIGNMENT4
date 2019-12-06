import unittest
from unittest import TestCase
import inspect
from menu_item_manager import MenuItemManager
from food import Food
from drink import Drink
from menu_item_stats import MenuItemStats
import os
from unittest.mock import patch, mock_open
from sqlalchemy import create_engine
from base import Base
import datetime

class Testmanager(unittest.TestCase):
    """ Unit tests for menu_item_managerr"""

    def setUp(self):
        """Set up for all the values"""

        engine = create_engine('sqlite:///test_menu.sqlite')

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.logPoint()

        self.kashmir_dosa = MenuItemManager('Kashmir Dosa', "test_menu.sqlite")

        self.barley_bread = Food("barley bread", 12, datetime.datetime.now(), 12.99, 149, "India", "Barley", "small",
                                 True)

        self.mango_lasi3 = Drink("mango lasis", 10, datetime.datetime.now(), 12.99, 80, "lasi producer ltd", 129.99,
                                 False, False)

        self.undefined_value = None
        self.empty_value = ""

    def test_team(self):
        """ 010A: Valid Construction """
        self.assertIsNotNone(self.kashmir_dosa, "Team must be defined")

    def test_add(self):
        """ 020A: Valid Add menu """

        self.assertIsNotNone(self.barley_bread, "Food must be defined")

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 1, "Menu has one item")


    def test_add_menu_already_exists(self):
        """ 020C: Invalid Add menu - Menu Already Exists """

        self.logPoint()

        self.assertEqual(len(self.kashmir_dosa.get_all()), 0, "Menu has no item")

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 1, " Menu must have 1 item")

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 1, "Menu must have 1 item")

    def test_remove_menu_item(self):
        """ 030A: Valid remove menu """

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.assertEqual(self.kashmir_dosa._restaurant_name, "Kashmir Dosa", "Id must be one")

        self.kashmir_dosa.remove_menu_item(1)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 0, "Must have no menu item")


    def test_delete_non_existent_menu(self):
        """ 030C: Invalid Delete Menu item - No id existent """

        self.kashmir_dosa.add_menu_item(self.barley_bread)

        menu = self.kashmir_dosa.get_by_id(1)

        self.assertEqual(menu.id, 1)

        self.assertRaisesRegex(ValueError, "id does not exist.",  self.kashmir_dosa.remove_menu_item, 4)
        self.assertEqual(len(self.kashmir_dosa.get_all()), 1, "menu must have one items")

    def test_get_by_id(self):
        """ 040A: Valid Get the menu wanted """

        self.kashmir_dosa.add_menu_item(self.barley_bread)

        menu = self.kashmir_dosa.get_by_id(1)

    def test_menu_exist(self):
        """050A: Valid menu exists"""
        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)

        self.assertTrue("needs to be true", self.kashmir_dosa.menu_exist(1))

    def test_get_all(self):
        """060A: Get all the menus"""
        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)

        list_menus = self.kashmir_dosa.get_all()

        self.assertEqual(list_menus[0], "barley bread", "needs to be barley bread")


    def get_all_menu_item(self):
        self.logPoint()
        """070A: Get all the menu item"""
        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.kashmir_dosa.add_menu_item(self.mango_lasi3)

        self.assertEqual(self.kashmir_dosa.get_all(), "['barley bread', 'mango lasis'] ",
                         "needs to be list of the items")

    def test_update(self):
        """ 080A: Valid Update """

        self.logPoint()

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.kashmir_dosa.add_menu_item(self.mango_lasi3)

        mango_lasi = Drink("mango lasi5", 8, datetime.datetime.now(), 6.99, 80, "lasi producer ltd", 129.99, False,
                           False)

        self.kashmir_dosa.update(2, mango_lasi)

        self.assertEqual(self.kashmir_dosa.get_all()[1], "mango lasi5")

    def test_get_menu_item_stats(self):

        self.logPoint()
        """090A Check the stats of the menu"""

        mango_lasi = Drink("mango lasi", 8, datetime.datetime.now(), 6.99, 80, "lasi producer ltd", 129.99, False,
                           False)

        self.kashmir_dosa.add_menu_item(self.barley_bread)
        self.kashmir_dosa.add_menu_item(self.mango_lasi3)
        self.kashmir_dosa.add_menu_item(mango_lasi)

        stats = self.kashmir_dosa.get_menu_item_stats()
        stats_dict = stats.to_dict()
        self.assertEqual(stats_dict['_total_num_menu_items'], 3)

    def tearDown(self):
        """ Create a test fixture after each test method is run """
        os.remove("test_menu.sqlite")
        self.logPoint()


    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


if __name__ == '__main__':
    unittest.main()