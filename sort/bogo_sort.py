import random


def in_order(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True


def bogo_sort(numbers):
    count = 0
    while not in_order(numbers):
        random.shuffle(numbers)
        count += 1
    return numbers, count


if __name__ == '__main__':
    print(bogo_sort([1, 6, 3, 2, 4, 5]))
    