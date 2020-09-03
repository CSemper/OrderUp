from functions.menu import main_menu, start_up, clear_screen, person_list, drink_list, order_list, preference_list
from classes.Person import Person as Person
from classes.Drink import Drink as Drink
from classes.Order import Order as Order
from classes.Preference import Preference as Preference

def add_people():
    name = input("Please enter the person's name:    ")
    age= input ("Please enter the person's age:   ")
    gender = input ("Please enter the person's gender:   ")
    person = Person(name, age, gender)
    person_list.append(person)
    return person_list

def add_drinks():
    kind = input("Please enter the name of the drink:   ")
    temp= input ("Is this drink hot, cold, or room temperature?:    ")
    drink= Drink(kind, temp)
    drink_list.append(drink)
    return drink_list