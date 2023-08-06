a = [3, 4, 5, 66, 98, 96, 75, 15, 36, 123, 68]
'''b = []

for i in a:
    if i%2 == 0:
        b.append(i)

print(b)'''

# another way : comprehension means it is way to create a new list from existing list
b = [i for i in a if i%2 == 0]
print(b)
# we can also create set
t = [1,2,4,3,6,5,1]
s = {i for i in t}
print(s)