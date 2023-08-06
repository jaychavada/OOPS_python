# if we use static method then no need of self
class Employee:
    company = "Google"

    def getSalary(self):
        print(
            f"Salary for employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning sir!")


jack = Employee()
jack.salary = 100000
jack.getSalary()
jack.greet()