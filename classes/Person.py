class Person:
    def __init__ (self, uid, first_name, age, fave_drink):
        self.uid=uid
        self.first_name=first_name
        self.age= age
        self.fave_drink=fave_drink

    
    def __repr__(self):
        return (f"ID: {self.uid}; Name: {self.first_name}; Age: {self.age}; Fave_Drink:{self.fave_drink}")