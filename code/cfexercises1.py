"""Demonstrate functions, conditionals, sorting and factorial methods.

Inputs are assumed to be non-negative real numbers for square roots,
comparable real numbers for comparisons, and small non-negative
integers for factorials. Invalid inputs are not explicitly checked.
"""


def foo_1(x):
    """Return the square root of a non-negative real number."""
    return x ** 0.5


def foo_2(x, y):
    """Return the larger of two real numbers."""
    if x > y:
        return x
    return y


def foo_3(x, y, z):
    """Return three real numbers in ascending order."""
    # Successive comparisons place the smallest value first, then order the rest.
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return [x, y, z]


def foo_4(x):
    """Return the factorial of a non-negative integer using a for loop."""
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result


def foo_5(x):
    """Return the factorial of a small non-negative integer recursively."""
    # The zero case gives 0! = 1 and terminates the recursive calls.
    if x == 0:
        return 1
    return x * foo_5(x - 1)


def foo_6(x):
    """Return the factorial of a non-negative integer using a while loop."""
    facto = 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto


if __name__ == "__main__":
    print("Square root of 9:", foo_1(9))
    print("Larger of 3 and 7:", foo_2(3, 7))
    print("Larger of 5 and 5:", foo_2(5, 5))
    print("Sorted values:", foo_3(3, 1, 2))
    print("Sorted values with duplicates:", foo_3(2, 1, 2))

    # Compare the three factorial methods, including zero and one.
    for x in [0, 1, 5]:
        print(
            "Factorials for", x, ":",
            foo_4(x), foo_5(x), foo_6(x)
        )