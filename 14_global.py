a = 54  # global variable


def func1():
    global a
    print(a)  # print global variable
    a = 8  # local variable
    print(a)


func1()
print(a)
