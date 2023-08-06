class MyClass:
    count = 0  # class variable

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Accessing the class method without creating an instance
print(MyClass.get_count())  # Output: 0

# Creating instances of the class
obj1 = MyClass()
obj2 = MyClass()

# Accessing the class method using the class itself
print(MyClass.get_count())  # Output: 2