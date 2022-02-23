"""Two statistic functions for list of floats."""
from unittest import result


def average(numbers: list[float]) -> float:
    """Average value."""
    return sum(numbers)/len(numbers)


def median(numbers: list[float]) -> float:
    """Median value."""
    length = len(numbers)
    if(length & 1 == 0):
        result = numbers[int(length/2)]+numbers[int(length/2)+1]
        result /= 2
    else:
        result = numbers[int(length/2)]
    return result
