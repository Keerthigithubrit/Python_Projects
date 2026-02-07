def temp_convert(t):
    unit = input("Enter the Unit(C or F):").strip().upper()
    if unit == 'C':
        convert_to_Farenheit = (temp * 9/5) + 32
        print(f"{temp} C is equal to {convert_to_Farenheit:.2f}F")
    elif unit == "F":
        convert_to_Celcius= (temp - 32) * 5/9
        print(f"{temp} F is equal to {convert_to_Celcius:.2f}C")
    else:
        print("Invalid Unit.Please enter C or F.")

temp = float(input("Enter the Temperature value:"))
temp_convert(temp)