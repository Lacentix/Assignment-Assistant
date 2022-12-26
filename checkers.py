def check_name(name):
    if not name.isalpha():
        raise ValueError("Name must not contain numbers or special characters.")


def check_id(id):
    if not id.isdigit() or len(id) != 9:
        raise ValueError("ID must be a 9-digit number.")
    for character in id:
        if character.isalpha():
            raise ValueError("ID must not contain letters.")
