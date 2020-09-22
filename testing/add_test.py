from classes.Person import Person as Person
from classes.Drink import Drink as Drink
from classes.Preference import Preference as Preference
from classes.Order import Order as Order

# def test_AddPerson():
#     test_person = Person("Chenyse", 25, "female")
#     expected_person_name = "Chenyse"
#     expected_person_age = 25
#     expected_person_gender = "female"
#     assert test_person.name == expected_person_name
#     assert test_person.age == expected_person_age
#     assert test_person.gender== expected_person_gender
    
def test_AddDrinks():
    test_add_drinks = Drink("lemonade", "cold")
    expected_drink_kind = "lemonade"
    expected_drink_temp = "cold"
    assert test_add_drinks.kind == expected_drink_kind
    assert test_add_drinks.temp == expected_drink_temp

def test_AddPreference():
    test_add_pref = Preference("Lisa", "hot chocolate", "extra-hot")
    expected_name= "Lisa"
    expected_fave="hot chocolate"
    expected_temp="extra-hot"
    assert test_add_pref.name == expected_name
    assert test_add_pref.fave == expected_fave
    assert test_add_pref.temp == expected_temp

def test_AddOrder():
    test_add_order = Order("Martin", "apple juice")
    expected_order_name = "Martin"
    expected_order_choice= "apple juice"
    assert test_add_order.name == expected_order_name
    assert test_add_order.choice == expected_order_choice