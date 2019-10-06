def my_min(numbers):
    smallest_so_far = None
    for num in numbers:
        if smallest_so_far is None:
            smallest_so_far = num
        elif num < smallest_so_far:
            smallest_so_far = num
    return smallest_so_far


def my_max(numbers):
    largest_so_far = None
    for num in numbers:
        if largest_so_far is None:
            largest_so_far = num
        elif num > largest_so_far:
            largest_so_far = num
    return largest_so_far


def my_average(numbers):
    sum = 0
    if len(numbers) == 0:
        average = None
    else:
        for num in numbers:
            sum += num
        average = sum / len(numbers)
    return average


def my_median(numbers):
    if len(numbers) == 0:
        median = None
    else:
        numbers.sort()
        index = int(len(numbers) / 2)
        if len(numbers) % 2 != 0:
            median = numbers[index]
        else:
            median = (numbers[index - 1] + numbers[index]) / 2
    return median


def my_range(numbers):
    if len(numbers) == 0:
        range = None
    else:
        range = my_max(numbers) - my_min(numbers)
    return range


def my_sample_variance(numbers):
    length = len(numbers)
    if length == 0:
        variance = None
    elif length == 1:
        variance = 0
    else:
        average = my_average(numbers)
        variance_sum = 0
        for num in numbers:
            variance_sum += (num - average) * (num - average)
        variance = variance_sum / (length - 1)
    return variance


def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line:
            lines.append(line)
    fhandle.close()
    return lines


if __name__ == '__main__':
    dataset = getFileLines('MH8811-04-Data.csv')
    numbers = []
    for data in dataset:
        numbers.append(int(data))
    print("Dataset:{}".format(numbers))
    min = my_min(numbers)
    print("Minimum Value:{}".format(min))
    max = my_max(numbers)
    print("Maximum Value:{}".format(max))
    average = my_average(numbers)
    print("Average:{}".format(average))
    median = my_median(numbers)
    print("Median:{}".format(median))
    range = my_range(numbers)
    print("Range:{}".format(range))
    variance = my_sample_variance(numbers)
    print("Sample Variance:{}".format(variance))
