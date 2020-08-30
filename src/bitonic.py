import math
def is_power_of_2(num):
    if num == 0:
        return False
    if math.ceil(math.log2(num)) == math.floor(math.log2(num)):
        return True
    return False

def bitonic_sort(arr):
    length = len(arr)
    if not is_power_of_2(length): raise ValueError("Should be log2")    
    gap = 1
    max_ = gap
    while  max_ <= length//2:
        while gap >= 1:
            order = True
            jump = 2 * gap
            start = 0
            i = 1
            while (start + jump <= length):
                comparisons = 0
                while (comparisons < gap):
                    if (order and arr[start + comparisons] > arr[start + comparisons + gap]) or (not order and arr[start + comparisons] < arr[start + comparisons + gap]):
                        arr[start + comparisons], arr[start + comparisons + gap] = arr[start + comparisons + gap], arr[start + comparisons]
                    comparisons += 1
                if (max_ - i == 0):
                    order = not order
                else: i += 1
                start += jump
            gap = gap // 2
        max_ *= 2
        gap = max_
    
    return arr

print(bitonic_sort([1, 3, 2, 4, 5, 2, 8, 6]))
