#!/bin/python3

import math
import os
import random
import re
import sys

# Passes 6/8 Test cases

def balancedSums(arr):

    if len(arr) == 1:
        return "YES"

    print(arr[:1])
    print(arr[1])
    print(arr[1 + 1:])

    for i in range(0, len(arr)):

        print("We are on number: ", arr[i])
        print(arr[:i])
        print(arr[i])
        print(arr[i + 1:])

        sum_left = sum(arr[:i])
        sum_right = sum(arr[i+1:])
        print("sum of left hand side is: ", sum_left)
        print("sum of right hand side is: ", sum_right)

        if sum_left == sum_right:
            return "YES"

    return "NO"




print(balancedSums([2]))