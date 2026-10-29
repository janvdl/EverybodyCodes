from math import ceil, sqrt, pow

# read input
debug = False
if debug:
    line = open('2026/01/input_sample.txt', 'r').readlines()[0]
else:
    line = open('2026/01/input_c.txt', 'r').readlines()[0]
values = [int(c) for c in line.split(',')]

# function to find diff with closest next circumference value
def next_diff(n):
    # square cone minimum is always some multiple of 8
    # sides must be odd so that there is only a single space open in the centre
    # 3x3 requires 8 cones
    # 5x5 requires 24
    # 7x7 requires 48
    # 9x9 requires 80

    # if the number of cones is represented by x^2 - 1
    # then we are looking for x^2 - 1 >= n
    # x = ceil(sqrt(n + 1)) and the ceil should round up to an odd number else + 1
    # and the solution is x^2 - 1, min of 8 cones

    root = sqrt(n + 1)
    x = ceil(root) if ceil(root) % 2 != 0 else ceil(root) + 1
    next = max(8, pow(x, 2) - 1) # a minimum of 8 cones is needed to have a single open space surrounded by cones
    diff = next - n

    return diff

# loop over all input values, find next square, and add up all the diffs
diffs = 0
for x in values:
    diffs += next_diff(x)

print(diffs)