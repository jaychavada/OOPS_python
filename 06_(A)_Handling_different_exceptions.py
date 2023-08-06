try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number"))
    c = a / b
    print(c)
except ValueError as e:
    print(f"Please Enter valid value! {e}")

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")

print("Thanks for using this code!")


# raising exceptions
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Not valid format")


a = increment(45)
print(a)

# another example
while (True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("Number greater than 6")
    except Exception as e:
        print(e)

print("Thanks for playing game")
