# In python, functions are first class, so can be assigned 
# to functions and passed to other functions as arguments.

# Functions as first order citizen
def add_one(x):
    return x + 1

def apply_function(f,x):
    return f(x)

f = add_one
x = 1

a = apply_function(f=f,x=x)

print(a)

# Functions as second order citizens
# A higher order function is simply a function 
# that has a function as an argument.

# Second order functions are useful when we notice 
# that two or more functions are the same 
# apart from some internal part 

def sum(data):
    result = 0
    for x in data:
        result = result + x
    return result


def maximum(data):
    result = 0
    for x in data:
        result = maximum(result,x)
    return result

# These are the same apart from the binary operation
# Lets define a second order function

x = sum
print(type(sum))

def reduce(data:list,bin_op):
    result = 0
    for x in data:
        result = bin_op(y=result,x=x)
    return result

print(reduce([1,2,3,4,-1], lambda y,x : y+x))

print(reduce([1,2,3,4,-1], lambda y,x : max(x,y)))