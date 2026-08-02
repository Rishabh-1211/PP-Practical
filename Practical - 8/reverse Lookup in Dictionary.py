d1 = {1: 'a', 2: 'b', 3: 'c'}

for x in d1:
    print(x, d1[x])


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k


k1 = reverse_lookup(d1, 'b')

print(k1)
