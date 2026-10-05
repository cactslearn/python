def decorator_function(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator_function
def say_hello():
    print("Hello!")


say_hello()