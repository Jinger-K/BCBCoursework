"""Demonstrate for loops, cumulative addition and a while loop."""

# Print integers from 0 to 4.
for i in range(5):
    print(i)

# Iterate over a list containing different data types.
my_list = [0, 2, "geronimo!", 3.0, True, False]
for k in my_list:
    print(k)

# Print the running total after each addition.
total = 0
summands = [0, 1, 11, 111, 1111]
for s in summands:
    total = total + s
    print(total)

# Increment before printing, producing integers from 1 to 100.
z = 0
while z < 100:
    z = z + 1
    print(z)