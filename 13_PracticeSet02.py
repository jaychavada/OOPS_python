# QUE: create a class C-2D vector and use it to create another class with 3D vector

class C2D_vec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class C3D_vec(C2D_vec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d = C2D_vec(1, 3)
v3d = C3D_vec(1, 9, 5)
print(v2d)
print(v3d)


# QUE: increment salary with use of getter setter and employee class we have to create
# salaryAfterIncrement = salary * increment
class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai / self.salary


e = Employee()
print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)
print(e.salaryAfterIncrement)


# QUE: Addition of complex number
class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"


c1 = Complex(1, 5)
c2 = Complex(8, 5)
print(c1 + c2)
