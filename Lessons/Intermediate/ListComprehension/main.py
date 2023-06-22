
numbers = [1,2,3]
# what are we doing
# for variable item
# in list
new_list = [n + 14 for n in numbers]

print(new_list)

name = "Daniel"
new_list = [letter for letter in name]
print(new_list)

my_range = range(1,5)
new_range = [n * 2 for n in my_range]
print(new_range)