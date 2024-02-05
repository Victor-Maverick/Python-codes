my_list = [10, 20, 30, 40, 50, 50, 60, 70, 80, 90]

def get_list_length(list1):
    count = 0
    for number in list1:
        count+=1
    return count


def get_list_sum_of_even_elements(list1):

    sum = 0
    for count in range(1, len(list1), 2):
        sum += list1[count]

    return sum


def get_list_sum_of_odd_index_elements(list1):
    sum = 0
    for count in range(0, len(list1), 2):
        sum += list1[count]

    return sum


def multiply_third_elements(list1):
    product = 1
    for count in range(0, len(list1), 2):
        product *= list1[count]

    return product


def get_list_total(list1):
    total = 0
    for count in range(len(list1)):
        total += list1[count]
    return total


def get_highest_in_list(list1):
    highest = 0
    for count in range(len(list1)):
        if list1[count] > highest:
            highest = list1[count]
    return highest


def get_lowest_in_list(list1):
    minimum = my_list[0]
    for count in range(len(list1)):
        if list1[count] < minimum:
            minimum = list1[count]
    return minimum


def get_common_strings(list1):
    list2 = []
    for count in range(len(list1)):
        first_character = list1[count][0]
        second_character = list1[count][-1]
        same_character = list1[count][0] == list1[count][-1]
        if len(list1[count]) >= 2 and same_character:
            list2.append(list1[count])
    return list2