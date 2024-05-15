# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/15/2024
# Description: Reverses the oder of elements in a list.
def reverse_list(vals):
    """Reverse the elements of a list."""
    left = 0
    right = len(vals) - 1
    while left < right:
        vals[left], vals[right] = vals[right], vals[left]
        left +=1
        right -=1