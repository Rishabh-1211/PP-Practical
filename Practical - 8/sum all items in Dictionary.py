my_dict = {'data1': 100, 'data2': 50, 'data3': 40}

s = 0

for i in my_dict.values():
    s += i

print(s)

# using sum function

print(sum(my_dict.values()))
