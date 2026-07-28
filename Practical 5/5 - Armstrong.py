# Armstrong number check
def is_armstrong(num):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** 3   # assuming 3-digit number
        temp //= 10

    if total == num:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

n = int(input("Enter a number: "))
is_armstrong(n)

