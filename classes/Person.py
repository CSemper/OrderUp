class Person:
    def __init__ (self, uid, first_name, surname):
        self.uid=uid
        self.first_name=first_name
        self.surname=surname

    
    def __repr__(self):
        return (f"ID: {self.uid} Name:{self.first_name} {self.surname})