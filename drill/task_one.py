my_set = set()

def collect_input():
    number = int(input('Enter a number: '))
    return number




def add_to_set():
    for count in range(10):
        number = collect_input()
        while number in my_set:
            number = collect_input()
            break
        my_set.add(number)

    print(my_set)

add_to_set()