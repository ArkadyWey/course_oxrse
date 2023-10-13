# MAP
# takes each value of iterable and applies function to it

iterable = [1,2,3]

result_lazy = map(lambda x : x**2, iterable) # uses lazy evaluation so need to convert 
result = list(result_lazy)

print(result)


# FILTER
# applies function with boolean output to each element of an iterable and returns same element if true

result_lazy = filter(lambda x : x>1, iterable)
result = list(result_lazy)

print(result)

# REDUCE 
# takes first two values, produces a result, uses this with the next, etc...

from functools import reduce
result_lazy = reduce(lambda x,y : x+y, iterable)

result = result_lazy
print(result)

# Sum of squares
def sum_of_squares(data):
    squares = map(lambda x:x**2, data)
    sos     = reduce(lambda x,y:x+y, squares)
    return sos

print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

# Sum of squares on list of strings
def sum_of_squares(data:list):
    #integers = [int(x) for x in data]
    integers = map(lambda x:int(x), data)
    squares = map(lambda x:x**2, integers)
    sos     = reduce(lambda x,y:x+y, squares)
    return sos

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))


# Sum of squares on list of strings with # removed
# NB:
x = "#100"
is_number = lambda x:x[0]!="#"
print(is_number(x))

def sum_of_squares(data:list):
    not_comments = filter(lambda x:x[0]!="#",data)
    integers = map(lambda x:int(x), not_comments)
    squares = map(lambda x:x**2, integers)
    sos     = reduce(lambda x,y:x+y, squares)
    return sos

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))