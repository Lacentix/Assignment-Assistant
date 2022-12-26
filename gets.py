def get_name():
    first_name = input("Enter your first name: ").capitalize()
    last_name = input("Enter your last name: ").capitalize()
    return first_name[0] + first_name[1:].lower(), last_name[0] + last_name[1:].lower()


def get_id():
    id = input("Enter your ID: ")
    return id
