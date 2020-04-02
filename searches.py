# TODO: Jump search, interpolation search, exponential search, sublist search
# TODO: Fiboonaci search, the ubiquitous binary search, unbound binary search
# TODO: binary search withouth recursion

def binary_search(val, ls):
    """
    Use log(n) complexity binary search for val in ls
    :param val: value to find in list ls
    :param ls: list of numbers to search through
    :return: index of first instance of val found in ls
    """
    num = len(ls)
    half = num // 2
    cur = ls[half]
    if cur == val:
        return half
    elif val > cur:
        return half + binary_search(ls[cur:], val)
    elif val < cur:
        return binary_search(ls[:cur], val)
