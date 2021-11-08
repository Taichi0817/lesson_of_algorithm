import random
from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers - 1):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 10000) for i in range(10)]
    print(bubble_sort(nums))











































