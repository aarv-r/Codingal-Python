class IOString():
    def __init__(self):
        self.strl = ""
    def get_string(self):
        self.strl = input("Enter a string")
    def print_string(self):
        print("result is", self.strl.upper())
strl = IOString()
strl.get_string()
strl.print_string()