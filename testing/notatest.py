# from Classes import Person, Drink, Preference
# import unittest

# class TestPerson (unittest.TestCase):
#     def test_case(self):
#         test_person = Person ("Chenyse", 25, "female")
#         expected_person_name = "Chenyse"
#         expected_person_age = 25
#         expected_person_gender = "female"
#         self.assertEqual(test_person.name, expected_person_name)
#         self.assertEqual(test_person.age, expected_person_age)
#         self.assertEqual(test_person.gender, expected_person_gender)


# class TestAddDrinks (unittest.TestCase):
#     def test_case2(self):
#         kind=input("Enter the kind of drink here:  ")
#         temp= "cold"
#         test_add_drinks = Drink(kind, temp)
#         expected_drink_kind = "lemonade"
#         expected_drink_temp = "cold"
#         self.assertEqual(test_add_drinks.kind, expected_drink_kind)
#         self.assertEqual(test_add_drinks.temp, expected_drink_temp)
        
# class TestAddPreference (unittest.TestCase):
#     def test_case3(self):
#         test_Preference= Preference("Chenyse", "lemonade", "cold")
#         expected_preference_name="Chenyse"
#         expected_preference_fave = "lemonade"
#         expected_preference_temp = "cold"
#         self.assertEqual(test_Preference.name, expected_preference_name)
#         self.assertEqual(test_Preference.fave, expected_preference_fave)
#         self.assertEqual(test_Preference.temp, expected_preference_temp)
        
# if __name__== "__main__":
#     unittest.main()  