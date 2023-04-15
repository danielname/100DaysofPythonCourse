#python uses the Mersenne Twister to pseudorandomly generate numbers
import random
random1_to10 = random.randint(1,10)
print(random1_to10)

# random is a python module
# a module is responsible for an item of functionality of your program
# import brings in the entire module (so be careful if anything autmatically runs, generally we only want values and called methods)

random_float = random.random()
print(random_float)
random0to5 = random.random() * 5
print(random0to5)