class Order:
    def __init__(self, name, choice):
        self.name= name
        self.choice = choice
    
    def __repr__ (self):
        return (f"Order: {self.name} wants a/an {self.choice}.")