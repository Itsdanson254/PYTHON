class Person:
    def __init__(self,firstname,age,gender):
        self.firstname =  firstname
        self.age = age
        self.gender = gender
    def details(self):
        print(self.firstname,"is studying")

teacher = Person("MRS Gateri",34,"Male")
accountant =Person("Mark Njiroine",29,"Male")
nurse =Person("Joan Lanoi",19,"Female")

print(teacher.firstname,teacher.age,teacher.gender)
print(accountant.firstname,accountant.age,accountant.gender)
print(nurse.firstname,nurse.age,nurse.gender)