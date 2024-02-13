# Class is a blue print of an object
#  An Object is an instance of a class

class Person:
    # Properties / Attributes /Characteristics
    age = 18
    name = "Danson"

    # Method / Function / Behaviour
    def talk(self):
        print("Person is talking")

teacher = Person()
print(teacher.name)
print(teacher.age)
teacher.talk()