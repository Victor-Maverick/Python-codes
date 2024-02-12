def sum_positoinal_elements(my_list: list):
    length = int(len(my_list) / 2)
    if len(my_list) % 2 == 0:
        return my_list[0] + my_list[length-1] + my_list[length] + my_list[-1]
    return my_list[0] + my_list[length] + my_list[-1]