# Set co,prehension are similar to list comprehensions
my_set = range(5)
new_set = {x**2 for x in my_set}
print(new_set)

# Dictionary comprehensions are useful to say what it was before and what it is now
iterable = [1,2,3]
new_dict = {i+1: i**2 for i in iterable}
print(new_dict)

# Generators are basically comprehensions for tuples 
new_gen = (i**2 for i in iterable)
print(new_gen)
print(list(new_gen))