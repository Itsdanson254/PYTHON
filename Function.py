# Inbuilt functiion
number = max(89, 70, 49, 125)
print(number)

x = min(78, 45, 34, 32, 65, 75, 76, 25, 734)
print(x)

z = pow(2, 3)
print(z)


# user defined function
def name():
    print("@galaxino.dantez")


name()  # calling a user defined function inorder to see the results


def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


# parameters/variables and argument
student()


def students(name, age, course):
    print(name, age, course)


students("victor Wainaia", 17, "Cybersecurity")
students("Kelvin Rommy", 18, "Datascience")
students("Merry chriss", 19, "MIT")
students("Terry Tommy", 18, "Cybersecurity")
students("John Adbi", 19, "Datascience")


def employees(Fullname, Age, Gender, Position, Salary):
    print(Fullname, Age, Gender, Position, Salary)

employees("Martin Kaiuki",18,"Male","Manager","50,000")
employees("Peter Gacheru",18,"Male","Treasure","45,000")
employees("Alvin Kibaara",18,"Male","Secretary","40,000")
employees("Boniface Mwangi",18,"Male","Chief Advisor","35,000")
employees("Jackson Maina",18,"Male","Member","30,000")
