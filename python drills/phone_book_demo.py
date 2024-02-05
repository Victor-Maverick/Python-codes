import phone_book
def phone_book_main():
    choice = int(input("""
                Welcome to your phoneBook.
        1-> Create new contact
        2-> Display contacts
        3-> Search contacts
        4-> Delete a contact
        5-> Delete all contacts
        Choose among the options 1 - 5 :
        """))
    return choice

def collect_phone_number():
    phone_number = str(input('Enter a number you want to save: '))
    return phone_number
def collect_contact_name():
    contact_name = str(input('Enter a name to save your contact: '))
    return contact_name

def collect_name_for_search():
    name = str(input('Enter name of contact you want to view: '))
    return name

def collect_name_to_delete():
    name = str(input('Enter a name of contact you want to delete: '))
    return name

def collect_number_to_delete():
    phone_number = str(input('Enter number you want to delete'))
    return phone_number

def search_phonebook():
    name = collect_name_for_search()
    for number in phone_book.contact_list:
        for key in number.keys():
            if name == key:
                print(number)


def contact_list():

    decision = phone_book_main()

    match decision:
        case 1:
            phone_book.add_contact(collect_contact_name(), collect_phone_number())
        case 2:
            phone_book.display_contact_list()
        case 3:
            search_phonebook()
        case 4:
            choice = int(input('1. delete by name\n2. delete by number'))
            match choice:
                case 1:
                    phone_book.delete_contact_by_name(collect_name_to_delete())
                case 2:
                    phone_book.delete_contact_by_number(collect_number_to_delete())
        case 5:
            phone_book.delete_list()
    contact_list()

contact_list()