
numbers = [1,2,3]
# what are we doing
# for variable item
# in list
new_list = [n + 14 for n in numbers]
print(new_list)

# strings
name = "Daniel"
new_list = [letter for letter in name]
print(new_list)

# on functions that produce lists
my_range = range(1,5)
new_range = [n * 2 for n in my_range]
print(new_range)

# conditional LC
names = ['Alex','Beth','Caroline','Dave','Eleanor', 'Freddie']
short_names = [listname for listname in names if len(listname) <= 4]
print(short_names)
# challenge
long_upper_names = [listname.upper() for listname in names if len(listname) > 4]
print(long_upper_names)
