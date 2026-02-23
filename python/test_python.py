num=input("Enter a number: ")
num2=int(input("Enter another number: "))
operation=input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The sum is: {num + num2}")
    case "-":
        print(f"The difference is: {num - num2}")
    case "*":
        print(f"The product is: {num * num2}")
    case "/":
        if num2 != 0:
            print(f"The quotient is: {num / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation.")