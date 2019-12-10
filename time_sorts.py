import timeit

# TODO: make into classes with time and sort propt.


def time_bubble_sort(rep):
    """

    :param rep: number of repetitions to be made
    :return: average time for executing bubble sort in milliseconds
    """
    bubble_time = timeit.timeit('bubble_sort(numbers)',
                                'from __main__ import numbers; '
                                'from sorts import bubble_sort',
                                number=rep) / rep
    return bubble_time * 1000  # milliseconds


def time_insertion_sort(rep):
    ins_time = timeit.timeit('insertion_sort(numbers)',
                             'from __main__ import numbers; '
                             'from sorts import insertion_sort',
                             number=rep) / rep
    return ins_time * 1000  # milliseconds


def time_selection_sort(rep):
    """

    :param rep: number of repetitions to be made
    :return: average time for executing bubble sort in milliseconds
    """
    selection_time = timeit.timeit('selection_sort(numbers)',
                                   'from __main__ import numbers; '
                                   'from sorts import selection_sort',
                                   number=rep) / rep
    return selection_time * 1000  # milliseconds


def time_pigeon_sort(rep):
    """

    :param rep: number of repetitions to be made
    :return: average time for executing bubble sort in milliseconds
    """
    pigeon_time = timeit.timeit('pigeon_hole_sort(numbers)',
                                'from __main__ import numbers; '
                                'from sorts import pigeon_hole_sort',
                                number=rep) / rep
    return pigeon_time * 1000  # milliseconds


def time_tim_sort(rep):
    tim_time = timeit.timeit('sorted(numbers)',
                             'from __main__ import numbers',
                             number=rep) / rep
    return tim_time * 1000
