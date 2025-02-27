def main():
    print("Hello, World!")
    
    name = input("What is your name? ")
    hello(name) # function call for 
    
    x = int(input("Enter the number: "))
    print(square(x)) # x * x
    
    
def hello(to):
    print("Hello, " + to + "!")

def square(x):
    return x * x
    # return x ** 2
    # return pow(x, 2)

main()