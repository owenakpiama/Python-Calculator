while True:
    # get the user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operator (+, -, *, /): ")

    # perform the calculation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero")
            continue
        result = num1 / num2
    else:
        print("Invalid operator")
        continue

    # print the result
    print("Result:", result)
    
    # ask the user if they want to perform another calculation
    choice = input("Do you want to perform another calculation? (y/n) ")
    if choice.lower() != 'y':
        break
