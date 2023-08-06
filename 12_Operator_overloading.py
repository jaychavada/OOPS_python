class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        print("Lets add")
        return self.num + other.num

    def __mul__(self, other):
        print("Lets multiply")
        return self.num * other.num

    # Dunder method
    def __str__(self):
        return f"Decimal number is {self.num}"

    def __len__(self):
        return 1


n1 = Number(4)
n2 = Number(5)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)

print(n1)  # This will invoke Dunder method
print(len(n1))
