import os

# Function for addition
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear Screen")
    print("6. Exit")


while True:
    show_menu()

    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result =", add(num1, num2))

            elif choice == '2':
                print("Result =", subtract(num1, num2))

            elif choice == '3':
                print("Result =", multiply(num1, num2))

            elif choice == '4':
                print("Result =", divide(num1, num2))

        except ValueError:
            print("Invalid input! Please enter numeric values only.")


    elif choice == '5':
        clear_screen()

    elif choice == '6':
        print("Thank you for using the calculator!")
        break

   
    else:
        print("Invalid choice! Please select a valid option.")