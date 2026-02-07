def palindrome(input_string):
    if input_string == input_string[::-1]:
        return "String is Palindrome"
    else:
        return "String is not palidrome"

# Get input string from user
input = input("Enter the string:")
result = palindrome(input)
print(result)