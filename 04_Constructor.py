class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):  # constructor
        self.name = name
        self.salary = 100
        self.subunit = subunit
        print("Employee is created!")
        
    def getDetails(self):
        print(f"Name of Employee is {self.name}")
        print(f"Salary of Employee is {self.salary}")
        print(f"Subunit of Employee is {self.subunit}")
        
    def getSalary(self):
        print(f"Salary for employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning sir!")


raj = Employee("Raj", 10000, "Youtube")
raj.getDetails()