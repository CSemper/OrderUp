class Drink:
    def __init__(self, kind, temp):
        self.kind = kind
        self.temp = temp
    
    def __repr__ (self):
        return (f"Drink: {self.kind} is a {self.temp} beverage.")