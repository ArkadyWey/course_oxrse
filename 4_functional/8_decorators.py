# A decorator is a higher order function that returns a function 

# let's decorate a function that adds oone to its argument 
# yb adding prints before and after, i.e., logging....

def add_one(x):
    return x + 1

my_func = add_one
#print(my_func(1))




# Create the decorator
def a_decorator(a_function):
    """
    This is a decorator for a_function
    """
    def an_inner(*args,**kwargs):
        """
        This is the inner function where we define
        what the decorator does. 
        """
        print("This is before the function. I will now evaluate the function.")
        result = a_function(*args,**kwargs)
        print("This is after the function is evaluated.")
        
        return result
    
    return an_inner


# Evaluating the decorator 
a_function = lambda x:x+1
a_decorated_function = a_decorator(a_function)
print(a_decorated_function(1))
    
# This is equivalent to... 
@a_decorator
def a_function(x):
    return x+1
a_decorated_function = a_function
print(a_decorated_function(1))





# Using decorators to time functions 

# Example.. here is a function to time 
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total


# Here is a decorator to time it
import time
def timer(func):
    def inner(func):
        start = time.process_time() # time in nanoseconds
        result = func
        stop = time.process_time()
        process_time_secs = (stop-start)
        print("Process took {} secs".format(process_time_secs))
        return result
    return inner

my_timer = timer(measure_me)
print(my_timer(5))
        



