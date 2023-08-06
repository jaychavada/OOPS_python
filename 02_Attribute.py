# class_Attribute

class Employee:
    company = "Google"
    salary = 200

jay = Employee()
dharmik = Employee()
print(jay.company)
print(dharmik.company)

# If we want to change name of company then....
Employee.company = "Youtube"
print(jay.company)
print(dharmik.company) 

#  Instance Attribute
jay.salary = 800
dharmik.salary = 500

print(jay.salary)
print(dharmik.salary)

# NOTE: first check instance attribute if it is available then it will print otherwise it will print class attribute.
# it will show error if there is no attribute of instance or class