# Ask User for their name and greet them

name = input("What is your name? ")


name1 = input("What is your name? ")
name2 = input("What is your last name? ")
name3 = input("What is your full name? ")


name4 = input("What is your name? ").strip().title() #perform multiple operations in one line

print("1] Hello," + name + "!")

print("2] Hello,", sep =" ", end = name1)
print(f"\n3] Hello, {name2}")


name3_1 = name3.strip() # remove white spaces both sides
#name3_1 = name3.lstrip() # remove white spaces from left
#name3_1 = name3.rstrip() # remove white spaces from right
name3_2 = name3.capitalize() # capitalize first letter
name3_3 = name3.upper() # capitalize all letters
name3_4 = name3.lower() # lower case all letters
name3_5 = name3.title() # capitalize first letter of each word
name3_6 = name3.swapcase() # swap case of each letter
name3_7 = name3.strip().title() # remove white spaces and Capitalize first letter of each word


print("Strip =",name3_1)
print("Capitalize =", name3_2)
print("Upper Case =", name3_3)
print("Lower Case =", name3_4)
print("Title =", name3_5)
print("Swap =", name3_6)
print("Strip and Title Together =", name3_7)


