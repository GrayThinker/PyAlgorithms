def interpolation_search(val, ls):
    #TODO: Implement
    pass


def exp_search(val, ls):
    #TODO: Implement
    pass


def sublist_search(val, ls):
    #TODO: Implement
    pass

def ternary_search(val, ls):
    #TODO: Implement
    pass

def dichotomous_search(val, ls):
    #TODO: Implement
    pass

def fib_search(val, ls):
    """divide and conquer approach
    time complexity: log(n)
    """
    fib_seq = [_ for _ in fib_lt(len(ls))]
    a = ls[0]
    b = ls[-1]
    # c = a + fib_seq[]

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)
    
def fib_lt(n):
    i = 0
    j = 1
    while(i < n):
        yield i
        i, j = j, i + j

def unbound_binary_search(val, ls):
    #TODO: Implement
    pass


def ubiq_binary_Search(val, ls):
    #TODO: Implement
    pass


def rec_binary_Search(val, ls):
    #TODO: Implement
    pass


def binary_search(val, ls):
    """
    Use O(log(n)) complexity binary search for val in ls
    :param val: value to find in list ls
    :param ls: list of numbers to search through
    :return: index of first instance of val found in ls
    """
    while len(ls) >= 1:
        half = len(ls) // 2
        if val == ls[half]:
            return half
        if val > ls[half]:
            ls = ls[half+1:]
        else:
            ls = ls[:half]
    return -1

def jump_search(val, ls):
    """
    Use O(sqrt(n))
    """
    block = round(len(ls)**.5)
    for i in range(0, len(ls), block):
        if ls[i] == val:
            return i
        if ls[i] < val:
            for ii in range(i, block):
                if ls[ii] == val:
                    return ii
    return -1       
