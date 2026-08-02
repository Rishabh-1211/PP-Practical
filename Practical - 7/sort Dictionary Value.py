my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

# Ascending sort by value
asc = sorted(my_dict.items(), key=lambda item: item[1])
print("Ascending:", asc)

# Descending sort by value
desc = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
print("Descending:", desc)
