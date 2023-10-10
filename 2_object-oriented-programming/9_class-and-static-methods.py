class Employee:
    # define some class attributes
    NO_OF_EMPLOYEES = 0

    def __init__(self, first_name, last_name, salary):
        # define some instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.increment_employees()
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def give_raise(self, amount):
        self.salary = self.salary + amount
        print("Number of employees is: ", Employee.NO_OF_EMPLOYEES) # use class name to access in instance method
        return self.salary
    
    @classmethod
    def employee_from_full_name(cls, full_name, salary):
        split_name = full_name.split(" ")
        first_name = split_name[0]
        last_name  = split_name[1]
        return cls(first_name=first_name, last_name=last_name, salary=salary) # creates a new class

    @classmethod 
    def increment_employees(cls):
        cls.NO_OF_EMPLOYEES = cls.NO_OF_EMPLOYEES + 1 # use cls variable to access in class method
    
    @staticmethod 
    def get_employee_legal_obligations(obligation_number): # cannot change the class or instance attributes since no self or cls
        legal_obligations = """
        1. An employee must complete 40 hours a week.
        2. ...
            """
        if obligation_number == 1:
            print("Obligation 1 is ...")
        elif obligation_number == 2:
            print("Obligation 2 is ...")
        else: 
            raise KeyError("No such obligation.")
        return "Here are all legal obligations: " + legal_obligations
    
alice = Employee("Alice", "Adams", 30_000)
print(alice.first_name) # first_name is an instance attribute
print(Employee.NO_OF_EMPLOYEES) # last_name is a class attribute 

# If I add another employee to the system... 
bob = Employee("Bob", "Benson", 20_000)

# then the class attribute is alterered globally
print(Employee.NO_OF_EMPLOYEES) # last_name is a class attribute - access using class name

alice.give_raise(5_000)
print(alice.employee_from_full_name("Alice Adams",alice.salary))

print(alice.get_employee_legal_obligations(1))