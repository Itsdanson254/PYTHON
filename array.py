courses = ["MIT", "Cybersecurity", "Datascience"]
print(courses)

# Accessing an element in array
print(courses[1])

# looping through an array
for courses in courses:
    print(courses)

# Adding an element to an array
courses.append("Android Development")
print(courses)

# Deleting an element in an array
courses.remove("Datascience")
print(courses)