import os


def check_name(name):
    if not name.isalpha():
        raise ValueError("Name must not contain numbers or special characters.")


def check_id(student_id):
    if not student_id.isdigit() or len(student_id) != 9:
        raise ValueError("ID must be a 9-digit number.")
    for character in student_id:
        if character.isalpha():
            raise ValueError("ID must not contain letters.")


def check_files_exist():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    found = False
    for file in files:
        if file.endswith(".pdf") or file.endswith(".doc") or file.endswith(".docx"):
            if os.path.isfile(os.path.join(cwd, file)):
                found = True
                break
    if not found:
        raise ValueError("Please add your assignments!")
