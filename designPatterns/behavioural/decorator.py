def decor_caps(func):
    def use_caps(*args, **kwargs):
        print("Before", args)
        new_args = [arg.upper() for arg in args]
        func(*new_args)

    return use_caps

@decor_caps
def print_args(a, b):
    print(a, b)

print_args("hi", "hello")


