class veichle:
    def __init__ (self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(veichle):
    pass

school_bus = bus("school volvo", 180, 12)
print("veichle name:", school_bus.name, "speed:", school_bus.max_speed, "mileage:", school_bus.mileage)