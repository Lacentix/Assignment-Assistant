from gets import get_name, get_id, get_subject_names
from checkers import check_name, check_id
from create import create_subject_folders, create_gitignore


def main():
    first_name, last_name = get_name()
    check_name(first_name)
    check_name(last_name)

    student_id = get_id()
    check_id(student_id)

    subject_names = get_subject_names()
    create_subject_folders(subject_names)
    create_gitignore(subject_names)


if __name__ == "__main__":
    main()
