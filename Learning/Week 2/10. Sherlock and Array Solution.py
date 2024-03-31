#!/bin/python3

import math
import os
import random
import re
import sys

# Better than my solution because:

"""
    Better than my solution because:
        - Efficiency: only calculates the total sum of the array once.
        - iterate through array using for num in arr. This is more Pythonic and concise
"""

def balancedSums(arr):
    sum_arr = sum(arr)
    left_sum = 0

    for num in arr:
        if left_sum == sum_arr - num - left_sum:
            return "YES"
        left_sum += num

    return "NO"


print(balancedSums([5, 6, 8, 11]))