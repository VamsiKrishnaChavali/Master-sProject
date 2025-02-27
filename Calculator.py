x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

x1 = int(x)
y1 = int(y)

print("The sum of the two numbers is: ", x + y)
print("The difference of the two numbers is: ", x - y)
print("The product of the two numbers is: ", x * y)
print("The division of the two numbers is: ", x / y)

print("The sum of the two numbers is: ", x1 + y1)
print("The difference of the two numbers is: ", x1 - y1)
print("The product of the two numbers is: ", x1 * y1)
print("The division of the two numbers is: ", x1 / y1)


z = (x + y)
z1 = z * 1000

print("Value of z is: ", end = " ")
print(f"{z:.2f}")

print("Value of z1 is: ", end = " ")
print(f"{z1}")
