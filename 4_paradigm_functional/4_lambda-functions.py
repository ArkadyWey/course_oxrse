
# Lambda are simple inline functions 

def use_func(f,x,y):
    return f(x,y)


result = use_func(lambda x, y : x*y+1, x=1,y=2)

print(result)

# It is BAD practice to set lambda to a variable 
# If we need to then why are we using one?
# e.g. 

l = lambda x,y : x*y+1

print(l)