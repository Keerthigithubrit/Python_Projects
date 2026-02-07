def calculator(num1,num2,operator):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        if num2 != 0:
            return num1/num2
        else:
            return "Error: Division by Zero"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Modulus by Zero"
    else:
        return "Invalid Operator"

# Get input from user
num1  = float(input("Enter the number1:"))
num2 = float(input("Enter the Number2:"))
operator = input("Enter operator (+,-,*,/,%):")

result = calculator(num1,num2,operator)
print(result)