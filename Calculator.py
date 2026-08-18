while True:
    try:
     num1 =  float(input("Enter first number: "))
     operator = input("Enter operator (+,-,*,/): ")
     num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers only")
        continue
    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divided by zero")
    else:
        print("Result:", "Invalid Operator")
    
    Choice = input("Do you want to continue, (yes/no): ")
    if Choice.lower() == "no":
        print("Calculator closed")
        break
        
    

