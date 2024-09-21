def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero!"
    else:
        return x / y

while True:
    print("\033[1mSelect operation:\033[0m ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit the program...")

    choice = input("\033[1mEnter choice(1/2/3/4/5): \033[0m")

    if choice > "5":
        print("\033[1mInvalid choice!!\n"
              "Enter a valid choice please!!...\033[0m")
        continue

    if choice == '5':
        print("\033[1mExited!!...\033[0m")
        break

    num1 = float(input("\033[1mEnter first number: \033[0m"))
    num2 = float(input("\033[1mEnter second number: \033[0m"))

    if choice == '1':
        print("\033[1m\nPerforming addition...\n"
              "The solution is ==>\033[0m", num1, "+", num2, "=", add(num1, num2), "\n")

    elif choice == '2':
        print("\033[1m\nPerforming subtraction...\n"
              "The solution is ==>\033[0m", num1, "-", num2, "=", subtract(num1, num2), "\n")

    elif choice == '3':
        print("\033[1m\nPerforming multiplication...\n"
              "The solution is ==>\033[0m", num1, "*", num2, "=", multiply(num1, num2),"\n")

    elif choice == '4':
        print("\033[1m\nPerforming division...\n"
              "The solution is ==>\033[0m", num1, "/", num2, "=", divide(num1, num2), "\n")