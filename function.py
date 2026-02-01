def first_function():
    print("Hello world")

# first_function()

def number_squared(number):
    print(number ** 2)

# number_squared(5)

def number_squared_custom(number, power):
    print(number ** power)

#number_squared_custom(3, 4)
arg_tuple =(5, 2, 3, 4, 5)
def number_args(*numbers):
    print(numbers[0] * numbers[1])

#number_args(arg_tuple)


def number_kwargs(**kwargs):
    print(kwargs['first'] + kwargs['second'])

number_kwargs(first=5, second=10)