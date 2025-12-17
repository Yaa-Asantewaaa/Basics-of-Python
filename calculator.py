import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    return math.sqrt(x) 
def power(x, y):
    return x ** y
print("Select operation:")
print("1. Add") 
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Power")
print("7. Modulus")
print("8. Floor Division")
while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
    if choice == '5':
            num1 = float(input("Enter number: "))
            print(f"Square root of {num1} = {square_root(num1)}")
    elif choice in ['1', '2', '3', '4', '6', '7', '8']:    
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '6':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '7':
                print(f"{num1} % {num2} = {num1 % num2}")
            elif choice == '8':
                print(f"{num1} // {num2} = {num1 // num2}")
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
            else:
                print("Invalid Input")
                
