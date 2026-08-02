colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Blue', 'Violet']

newlist = []

for i in colors:
    if colors.index(i) == 0 or colors.index(i) == 2 or colors.index(i) == 4 or colors.index(i) == 5:
        continue
    else:
        newlist.append(i)

print(newlist)