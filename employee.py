class Employee():
    """A sample class"""
    def __init__(self, first, last, salary):
        """A method that takes name and salary"""
        self.firsr_name = first
        self.last_name = last
        self.salary = salary

    def give_raise(self, amount = 5000):
        """a method to give raise to employees"""
        self.salary += amount
