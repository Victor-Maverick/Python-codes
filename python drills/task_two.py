sample_list = list(range(10, 20))


def get_length(sample_list):

    count = 0
    for number in sample_list:
        count += 1
    return count


def get_even_sum(sample_list):
    return sum(sample_list[::2])


def get_odd_sum(sample_list):
    return sum(sample_list[1::2])