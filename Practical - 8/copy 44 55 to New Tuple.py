tuple1 = (11, 22, 33, 44, 77, 88, 55, 44, 66)

tuple2 = ()

for x in tuple1:
    if x == 44 or x==55:
        tuple2 = tuple2 + (x,)

print(tuple2)
