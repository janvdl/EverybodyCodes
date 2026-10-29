from math import ceil, sqrt, pow

# read input
debug = False
if debug:
    line = open('2026/01/input_sample.txt', 'r').readlines()[0]
else:
    line = open('2026/01/input_b.txt', 'r').readlines()[0]
values = [int(c) for c in line.split(',')]

# function to find diff with closest next circumference value
def next_circum_diff(n):
    # circumference of square in the problem is always some multiple of 4
    # with a minimum value of 8 cones required to have an empty space in the middle
    # 3x3 requires 8 cones
    # 4x4 requires 12 cones
    # 5x5 requires 16 cones, etc.
    quotient = n / 4

    # the next value must have at least one empty space, so 3x3 (8 cones) is the min
    next = max(8, ceil(quotient) * 4)
    diff = next - n

    return diff

# loop over all input values, find next square, and add up all the diffs
diffs = 0
for x in values:
    diffs += next_circum_diff(x)

print(diffs)