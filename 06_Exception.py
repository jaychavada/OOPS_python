# try...except
try:
    x = int(input("What is x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not integer")

# try....except....else

try:
    x = int(input("What is x?"))
except ValueError:
    print("x is not integer")
else:
    print(f"x is {x}")

# use of while in try...except
while True:
    try:
        x = int(input("What is x?"))
    except ValueError:
        print("x is not integer")
    else:
        break

print(f"x is {x}")

# try....except...with finally
try:
    i = int(input("Enter a number: "))
    c = 1 / i
except Exception as e:
    print(e)
    exit()
finally:
    print("we are done")