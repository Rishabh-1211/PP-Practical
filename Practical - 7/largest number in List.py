def maxNum(numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum

print(maxNum([1, 2, -8, 0]))

# Using max() function

list1 = [1, 2 , 14, 6, 11]
print(max(list1))
