class Employee:
    def __init__(self):
        print("The employee object is created")
    def __del__(self):
        print("The employee object is destroyed")
obj = Employee()
del obj
print(obj)