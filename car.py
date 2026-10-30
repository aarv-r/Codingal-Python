class car:
    def __init__(self, mileage, max_speed):
        self.mileage = mileage
        self.max_speed = max_speed
object = car(50, 200)
print("This car has a mileage of", object.mileage, "and a max speed of", object.max_speed,".")
