# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Variable length argument
def f1(*n):
    # Use a breakpoint in the code line below to debug your script.
    print("Variable length argument")  # Press Ctrl+F8 to toggle the breakpoint.
    # Variable length argument is of type tuple
    print(type(n))
    print(n)

# Method to find sum of 2 numbers


def sum_using_vararg(*n):
    total = 0
    for x in n:
        total = total+x
    print(f"The sum of {n} is :{total}")

# Using both positional and var arg


def f2(x, *y):
    print(f"The positional arg {x}")
    print(f"The variable length argument {y}")


# Method using first var arg and then positional argumnet

def f3(*x, y):
    print(f"The var arg {x}")
    print(f"The keyword argument {y}")

# Can function take more then one variable length argument

def f4(*x, *y):
    print(x)
    print(y)

    # Error as File "C:\Users\kavya.p\PycharmProjects\pythonProject2\main.py", line 39
    #     def f4(*x, *y):
    #                ^
    # SyntaxError: * argument may appear only once

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Call f1 without any arguments
    # f1()
    # Call f1 with 1 arguments
    # f1(10)
    # Call f1 with 2 arguments
    # f1(10, 20, 30)
    # Tuple of tuple
    # f1((10, 20), (10, 20, 30, 40))
    # Sum of 0
    # sum_using_vararg()
    # Sum of 10
    # sum_using_vararg(10)
    # Sum of 10,20,30
    # sum_using_vararg(10, 20, 30)
    # Using both positional argument
    # f2(10, 20, 30, 40)
    # If we are calling method having both positional argument and var arg
    # then we have pass value of positional argument compulsory
    #f2(10, 20)
    # If we are calling method having both positional argument and var arg
    # then it's ok if we don't  pass value for var arg
    # f2(10)
    # f3(10, 20, 30)
    # Above throws the error Traceback (most recent call last):
    #   File "C:\Users\kavya.p\PycharmProjects\pythonProject2\main.py", line 63, in <module>
    #     f3(10, 20, 30)
    # TypeError: f3() missing 1 required keyword-only argument: 'y'
    # So ,fix this error
    f3(10, 20, 30, y=40)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
