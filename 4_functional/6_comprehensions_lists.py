# We can use list comprehensions to replicate map, filter, reduce

# MAP
iterable = [1,2,3]

square = lambda x:x**2
mapped = [square(x) for x in iterable]
mapped = [x**2 for x in iterable]
print(mapped)

# FILTER
filtered = [x for x in iterable if x>1]
print(filtered)

# REDUCE
# can't be done, since list comprehension returns a list