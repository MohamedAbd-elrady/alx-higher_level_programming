#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    ls = list_of_integers
    beg = 0
    end = len(ls)-1

    if ls[beg] > ls[beg+1]:
        return ls[beg]
    if ls[end] > ls[end-1]:
        return ls[end]

    mid = (beg+end)//2
    if ls[mid-1] < ls[mid] and ls[mid+1] < ls[mid]:
        return ls[mid]
    if ls[mid] < ls[mid-1]:
        return find_peak(ls[beg:mid+1])
    elif ls[mid] < ls[mid+1]:
        return find_peak(ls[mid:end+1])
    else:
        return ls[beg]
