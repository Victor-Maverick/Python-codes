def remove_item(my_set: set, number):
    if number in my_set:
        my_set.remove(number)
        return number

    return None