#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


from re import X


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    x = list_of_integers
    beg = 0
    end = len(x)-1

    if x[beg] > x[beg+1]:
        return x[beg]
    if x[end] > x[end-1]:
        return x[end]

    mid = (beg+end)//2
    if x[mid-1] < x[mid] and x[mid+1] < x[mid]:
        return x[mid]
    if x[mid] < x[mid-1]:
        return find_peak(x[beg:mid+1])
    elif x[mid] < x[mid+1]:
        return find_peak(x[mid:end+1])
    else:
        return x[beg]
