from math import ceil, sqrt, pow

# read input
debug = False
if debug:
    line = open('2026/01/input_sample.txt', 'r').readlines()[0]
else:
    line = open('2026/01/input_a.txt', 'r').readlines()[0]
values = [int(c) for c in line.split(',')]

# function to find diff with closest next square value
def next_square_diff(n):
    root = sqrt(n)
    next = pow(ceil(root), 2)
    diff = next - n

    return diff

# loop over all input values, find next square, and add up all the diffs
diffs = 0
for x in values:
    diffs += next_square_diff(x)

print(diffs)