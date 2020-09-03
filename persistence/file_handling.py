import csv
from classes.Person import Person as Person
from classes.Drink import Drink as Drink
from classes.Order import Order as Order
from classes.Preference import Preference as Preference

person_list =[]
drink_list = []
order_list = []
preference_list = []

def get_people(filename):
    with open(filename, "r+") as new:
        read_file= csv.reader(new, delimiter=',', quoting=csv.QUOTE_ALL)
        next(read_file)
        for line in read_file:
            new_person = Person(line[0], line[1], line[2])
            person_list.append(new_person)
 
def get_drinks(filename):
    with open(filename, "r+") as newx:
        read_filex= csv.reader(newx, delimiter= ",", quoting=csv.QUOTE_ALL)
        next(read_filex)
        for line in read_filex:
            new_drink = Drink(line[0], line[1])
            drink_list.append(new_drink)

def get_orders(filename):
    with open(filename, "r+") as newz:
        read_filez= csv.reader(newz, delimiter= ",", quoting=csv.QUOTE_ALL)
        next(read_filez)
        for line in read_filez:
            new_order = Order(line[0], line[1])
            order_list.append(new_order)

def get_preferences(filename):
     with open(filename, "r+") as newy:
        read_filey= csv.reader(newy, delimiter= ",", quoting=csv.QUOTE_ALL)
        next(read_filey)
        for line in read_filey:
            new_preference = Preference(line[0], line[1], line[2])
            preference_list.append(new_preference)

def save_people (filename):
    with open(filename, "w+") as save:
        save_file= csv.writer(save, quoting=csv.QUOTE_NONE, escapechar=' ')
        for person in person_list:
            save_file.writerow([person.name, person.age, person.gender])
        save.close()

def save_drinks (filename):
    with open(filename, "w+") as savex:
        save_filex= csv.writer(savex, quoting=csv.QUOTE_NONE, escapechar=' ')
        for drink in drink_list:
            save_filex.writerow([drink.kind, drink.temp])
        savex.close()

def save_order (filename):
    with open(filename, "w+") as savez:
        save_filez= csv.writer(savez, quoting=csv.QUOTE_NONE, escapechar=' ')
        for order in order_list:
            save_filez.writerow([order.name, order.choice])
        savez.close()
  
def save_preferences (filename):
    with open(filename, "w+") as savey:
        save_filey= csv.writer(savey, quoting=csv.QUOTE_NONE, escapechar=' ' )
        for preference in preference_list:
            save_filey.writerow([preference.name, preference.fave, preference.temp])
        savey.close()