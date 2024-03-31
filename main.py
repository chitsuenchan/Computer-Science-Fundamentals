# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def plusMinus(arr):

    positives = 0
    negatives = 0
    zeros = 0

    for num in arr:
        if num > 0:
            positives += 1
        if num < 0:
            negatives += 1
        if num == 0:
            zeros += 1

    print(positives/len(arr))
    print(negatives/len(arr))
    print(zeros/len(arr))




    print(arr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [1, 1, 0, -1, -1]

    plusMinus(arr)
