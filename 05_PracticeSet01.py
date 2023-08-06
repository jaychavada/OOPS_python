# QUE 01:
class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"Name of programmer is {self.name} and the product is {self.product}")

    @staticmethod
    def greet():
        print("Good Morning sir!")


hermione = Programmer("Hermione", "Skype")
ginny = Programmer("Ginny", "Github")

hermione.getInfo()
ginny.getInfo()
hermione.greet()

# QUE 02:


class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"Square of {self.number} is {self.number **2}")

    def squareRoot(self):
        print(f"SquareRoot of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"Cube of {self.number} is {self.number **3}")

a = Calculator(3)
a.square()
a.squareRoot()
a.cube()

# QUE 03:


class Sample:
    a = "Jack"  # class Attribute


obj = Sample()
obj.a = "Perl"  # instance Attribute

print(Sample.a)
print(obj.a)

# QUE 04:


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"Name of train is {self.name}")
        print(f"Seats on train is {self.seats}")

    def fareInfo(self):
        print(f"Price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(
                f"Your ticket has been booked! and seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry train is full")


jabalpur = Train("Jabalpur Express: 156363", 90, 500)
jabalpur.getStatus()
jabalpur.bookTicket()
jabalpur.fareInfo()
jabalpur.getStatus()