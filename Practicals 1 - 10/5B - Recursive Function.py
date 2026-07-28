# Practical 5B - Recursive Function

def factorial(n):  

    if n == 0 or n == 1:  

        return 1  

    elif n < 0:  

        return "Invalid Input"  

    else:  

        return n * factorial(n - 1) 

x = int(input("Enter number : "))


print(factorial(x)) 