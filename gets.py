from re import match


def get_name():
    first_name = input("Enter your first name: ").capitalize()
    last_name = input("Enter your last name: ").capitalize()
    return first_name[0] + first_name[1:].lower(), last_name[0] + last_name[1:].lower()


def get_id():
    student_id = input("Enter your ID: ")
    return student_id


def get_subject_names():
    subjects = (
        input("Enter a list of subjects separated by commas: ").strip().split(",")
    )
    for subject in subjects:
        if not match(r"^[A-Za-z]{3,4}[0-9]{3}$", subject):
            raise ValueError(
                "Subject names must be in the format 'abc123' or 'ABC123'."
            )
    return [subject.upper() for subject in subjects]
