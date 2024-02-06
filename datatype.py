# Data types
number = 45  # int
num = 56.76  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool


# variable storing multiple values
languages = ["python", "php", "java"]  # list
fruits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "Bangladesh", "USA"}  # set
# Dictionary
details = {
    "firstname": "Grace",
    "age": 17,
    "course": "MIT",
    "Nationality": "North America"
}
print(number)
print(greeting)
print(countries)
print(isPythonInteresting)
print(details)
print(details["course"])
print(details["Nationality"])
# Determining the data type
print(type(details))
print(type(countries))
print(type(fruits))
# Type casting - converting one data type to another

print(float(number))
print(int(num))
