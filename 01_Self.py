# SELF CAN ACCESS INSTANCE AND CLASS ATTRIBUTES

# Number class
class Number:
    def sum(self):
        return self.a + self.b


num = Number()
num.a = 12
num.b = 12
s = num.sum()
print(s)

# RailwayForm class
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
    
jaysApplication = RailwayForm()
jaysApplication.name = "Harry Potter"
jaysApplication.train = "Hogwarts"
jaysApplication.printData()
 
# Gaming class
class Gaming:
    module: "Gaming"
    def gameData(self):
        print(f"Name of game is {self.name}")
        print(f"Version of game is {self.version}")
    
startGame = Gaming()
startGame.name = "GTA-VICECITY"
startGame.version = "Beta 2.0"
startGame.gameData() 

# Employee class
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for employee working in {self.company} is {self.salary}")
    
jack = Employee()
jack.salary = 100000
jack.getSalary()