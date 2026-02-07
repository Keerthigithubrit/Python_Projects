def string_reverse(input):
    reversed_string = input[::-1]
    return reversed_string
user_input = input("Enter the string:")
result = string_reverse(user_input)
print(result)