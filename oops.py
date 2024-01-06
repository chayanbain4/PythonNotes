#How to define a class?

class MyClass:
    a = 10
    def func(self):     #self is a reference to the class instance, by using self we can access the attributes and methods of the class
        print('Hello')

# How to create an object?
obj = MyClass()
print(obj.a)
obj.func()


class Number:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b

n1 = Number()
sum = n1.add(2,3)
print(sum)

product = n1.multiply(2,5)
print(product)




class MyClass:
    def __init__(self, p1 = 0, p2 = 0):
        self.a = p1
        self.b = p2

o1 = MyClass(2,3)

print(o1.a, o1.b) #output: 2, 3

o2 = MyClass()

print(o2.a, o2.b) #output: 0, 0



# Find Distance between Origin and a Point

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2)**0.5
    
p1 = Point(6,8)
distance = p1.distance()
print(distance)



#--------------------------------------------------------------------------------------------------------------
#How to Delete an atrribute of an object?

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2)**0.5
    
p1 = Point(6,8)
print((p1.x , p1.y))

#1 : Delete Object
del p1
print(p1)

#2 : Delete Attribute
del p1.y
print(p1.y)