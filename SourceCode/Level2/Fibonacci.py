def fibonacci_seq(num):
    a, b = 0, 1
    for i in range(num):
        # print value sequence
        print(a,end = " ")
        # update a nd b value
        a, b = b,a+b
        
# get input from user
user_input = int(input("Enter the number:"))
fibonacci_seq(user_input)
    