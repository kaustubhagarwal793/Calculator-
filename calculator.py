print(" Calculator (type 'q' to quit) ")

while True:
    first = input("Enter first number: ")
    if first.lower() == "q":
        break
    operator = input("Enter operator (+, -, *, /): ")
    second = input("Enter second number: ")

    try:
        num1, num2 = float(first), float(second)
    except ValueError:
        print("Please enter valid numbers!\n")
        continue

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!\n")
            continue
        result = num1 / num2
    else:
        print("Invalid operator!\n")
        continue

    print("Result:", int(result) if result.is_integer() else result, "\n")