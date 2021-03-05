class Car:
    """initializing a Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} of miles")

    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else :
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:

    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """initialiize the battery's attribute"""
        self.battery_size = battery_size

    def describe_battery(self):
        """describing batterybwith print """
        print(f"This car has a {self.battery_size}-Kwh battery")

    def get_range(self):
        """Print a statement about the range"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge")




class ElectricCar(Car):

    """Represents the aspects of cars similar to which of electric car"""

    def __init__(self, make, model, year):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()


    def describe_battery(self):
        """Showing the percentage of a battery"""
        print(f"This car has the of {self.battery_size}-Kwh battery")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.get_range()