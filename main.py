# Task 1 Sample solution
# Given two sides of right angled triangle
# Calculate the third side. Get two sides from
# the user

ab = float(input("Please enter the first side: "))
bc = float(input("Please enter the second side: "))

ac =(ab**2 + bc**2)**(1/2)
print("The third side of the triangle equals: "+ str(ac))

# Part 2 task 1
ab = float(4)
bc = float(3)
height = ab
base = bc
area = (height * base) / 2
print(area)

print("The area of the triangle is: " + str(bin(int(area))))

# Task 2

my_numbers = [2,56,12,67,1000, 32,89,29,44,39,200,11,21]
a = min(my_numbers)
b = max(my_numbers)
print("minimum number of my list " + str(min(my_numbers)))
print("maximum number of my list " + str(max(my_numbers)))



