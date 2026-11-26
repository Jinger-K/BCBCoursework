"""Demonstrate loops, conditionals and break through printed messages.

Examples use integer arguments and valid terminating starting values.
Input conditions are documented but are not explicitly validated.
"""


def hello_1(x):
    """Print hello for multiples of three in range(x)."""
    for j in range(x):
        if j % 3 == 0:
            print("hello")
    print(" ")


def hello_2(x):
    """Print hello when either remainder condition is satisfied."""
    for j in range(x):
        # elif prevents two prints when both conditions are satisfied.
        if j % 5 == 3:
            print("hello")
        elif j % 4 == 3:
            print("hello")
    print(" ")


def hello_3(x, y):
    """Print hello for each integer in range(x, y)."""
    for i in range(x, y):
        print("hello")
    print(" ")


def hello_4(x):
    """Print hello while advancing to 15 in steps of three.

    Requires an integer x <= 15 with (15 - x) divisible by three.
    """
    while x != 15:
        print("hello")
        x = x + 3
    print(" ")


def hello_5(x):
    """Advance an integer x to 100, printing at selected values."""
    while x < 100:
        if x == 31:
            for k in range(7):
                print("hello")
        elif x == 18:
            print("hello")
        x = x + 1
    print(" ")


def hello_6(x, y):
    """Print numbered greetings until incrementing y reaches six.

    Examples use a Boolean x and an integer y < 6.
    If x is False, the loop is skipped.
    """
    while x:
        print("hello! " + str(y))
        y += 1
        # Exit this loop once the incremented value reaches six.
        if y == 6:
            break
    print(" ")


if __name__ == "__main__":
    hello_1(12)
    hello_2(12)
    hello_3(3, 17)
    hello_4(0)
    hello_5(12)
    hello_6(True, 0)