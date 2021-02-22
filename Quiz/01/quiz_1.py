# Written by *** for COMP9021
#
# Given a sequence L of numbers, the greedy increasing subsequence of L,
# say G, is inductively defined as follows:
# - If L is of length at most 1 then G is L.
# - If L is of the form (e_0, e_1, ..., e_n) with n >= 1, then:
#   - either e_1 is greater than e_0, in which case G is e_0 followed by the
#     greedy increasing subsequence of (e_1, ..., e_n),
#   - or e_1 is less than or equal to e_0, in which case G is the greedy
#     increasing subsequence of (e_0, e_2,..., e_n).
#
# 1. Generates a random list L of digits whose length is chosen by the user
#    (done).
# 2. Displays L (done),
# 3. Displays the integer made from these digits (without the leading 0s,
#    if any).
# 4. Graphically displays the greedy increasing subsequence of L as
#    horizontal bars.
# 5. Graphically displays the nonzero values in L as steps.


from random import seed, randrange
import sys

try:
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                              ).split()
                        )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(10) for _ in range(length)]
print('Here are the generated digits:', values)
# INSERT CODE HERE:
from itertools import accumulate
number = str(int(''.join((str(x) for x in values))))
print(f"\nThe integer made from these digits is: {number}\n")
print('Here is the greedy increasing subsequence of values, '
      'horizontally displayed:\n'
      )
# INSERT CODE HERE:
for item in sorted(set(accumulate(values, max)) - {0}):
    print("    " + "-" * item)

print('\nHere are the nonzero values, displayed as stairs:\n')
# INSERT CODE HERE:
# 第三问
for index, item in enumerate(accumulate(values)):
    if values[index] > 0:
        print("     " + ' ' * (item - values[index]) + '-' * values[index])