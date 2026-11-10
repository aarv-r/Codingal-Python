class bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
    def display(self):
        print(self.name)
        print(self.wingspan)
class penguin(bird):
    def __init__(self, name, wingspan, crest_colour):
        self.crest_colour = crest_colour
        super().__init__(name,wingspan)
superpenguin = penguin("Emperor penguin", 1.2, "black and white")
superpenguin.display() 
print(superpenguin.crest_colour)