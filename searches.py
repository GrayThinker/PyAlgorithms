

def binary_search(val, ls):
    """

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
