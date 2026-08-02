my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

# Ascending sort by value 

asc = sorted(my_dict.items()) 
print("Ascending:", asc) 

# Descending sort by value 

desc = sorted(my_dict.items(), reverse=True) 
print("Descending:", desc)
