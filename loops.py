# While loop
# Incrementing
number = 5
while number <= 10:
    print(number)
    number += 1

# Decrement
number2 = 105
while number2 >= 100:
    print(number2)
    number2 -= 1

# Break statement
x = 20
while x <= 25:
    print(x)
    if x == 24:
        break
    x += 1

# Continue statement while skipping
y = 79
while y <= 85:
    y += 1
    if y == 83:
        continue
    print(y)

#  For loop
languages = ["python","Java","C++"]
for r in languages:
    print(r)

# Range
for mynumber in range (9):
    print(mynumber)

for mynumb in range(2,9):
    print(mynumb)

for count in range(20,34,2):
    print(count)