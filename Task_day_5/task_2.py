'''2. Write a decorator function that will record the number of times a function is called. Your decorator function should be called record_calls and call_count attribute that keeps track of the number of times it was called.'''

def record_calls(func):
    def wrapper(x):
        wrapper.call_count += 1
        return func(x)
    wrapper.call_count = 0
    return wrapper

@record_calls
def my_function(x):
    print("Hello, world!")

my_function(10)
my_function(20)
print(my_function.call_count)