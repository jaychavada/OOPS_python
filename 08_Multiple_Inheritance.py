# MULTIPLE INHERITANCE : two parents one child

class Employee:
    company = "Visa"
    eCode = 120


class FreeLancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, FreeLancer):
    name = "Jay"


p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)