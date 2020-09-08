import os 
import csv

from persistence.file_handling import get_people, get_drinks, get_orders, get_preferences
from persistence.file_handling import person_list, drink_list, order_list, preference_list

def clear_screen():
    os.system("clear")
              
def main_menu():
    menu_text= """\n Please select one of the options below:\n
    [1] View/Edit People List
    [2] View/Edit Drink List
    [3] Order a Round of Drinks
    [4] View Orders & Receipt
    [5] View Preferences
    [6] Save & Exit"""
    print(menu_text)

def start_up():
    get_people("person_output.csv")
    get_drinks("drink_output.csv")
    get_orders("order_output.csv")
    get_preferences("preferences_output.csv")
    return person_list, drink_list, order_list, preference_list
    
