contact_list = []


def length_of_contact_list():
    return len(contact_list)

def delete_list():
    if len(contact_list) > 0:
        del contact_list[:]
    else:
        print('no contacts found')
def add_contact(name, phone_number):
    numbers = {}
    numbers.update({name: phone_number})
    if numbers not in contact_list:
        contact_list.append(numbers)



def delete_contact_by_name(name):
    if len(contact_list) > 0:
        for number in contact_list:
            for key in number.keys():
                if name == key:
                    contact_list.remove(number)
                else:
                    print('contact does not exist')
    else:
        print('no contacts')

def delete_contact_by_number(phone_number):
    if len(contact_list) > 0:
        for number in contact_list:
            for value in number.values():
                if phone_number == value:
                    contact_list.remove(number)
                else:
                    print('contact does not exist')
    else:
        print('no contacts')

def display_contact_list():
    if len(contact_list) > 0:
        for number in contact_list:
            for key, value in number.items():
                print('name', {key}, {value})