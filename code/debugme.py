"""Demonstrate handling division by zero during a loop.

This teaching example returns the last successful division result,
not a result for the failed division. The demonstration uses x = 20.
"""


def buggyfunc(x):
    """Print successful divisions and handle division by zero.

    Intended for positive integer demonstration inputs of at least two.
    Other inputs are not validated.
    """
    y = x
    for i in range(x):
        try:
            y = y - 1
            z = x / y
        except ZeroDivisionError:
            print("The result of dividing a number by zero is undefined")
        else:
            print(f"OK; {x = }; {y = }, {z = }")

    # The failed division leaves z holding the last successful result.
    return z


if __name__ == "__main__":
    print("Returned value:", buggyfunc(20))