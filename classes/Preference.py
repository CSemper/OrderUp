class Preference:
    def __init__(self, name, fave, temp):
        self.name=name
        self.fave=fave
        self.temp=temp
    
    def __repr__(self):
        return (f"Preference Recorded: {self.name} prefers a {self.temp} {self.fave}.")