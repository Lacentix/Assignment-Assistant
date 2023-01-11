from checkers import check_files_exist, check_id, check_name
from create import create_gitignore, create_subject_folders
from file_util import *
from gets import get_id, get_name, get_subject_names


def main():
    first_name, last_name = get_name()
    check_name(first_name)
    check_name(last_name)

    student_id = get_id()
    check_id(student_id)
    check_files_exist()

    subject_names = get_subject_names()
    create_subject_folders(subject_names)
    create_gitignore(subject_names)
    search_keywords_in_files(first_name, last_name, student_id)


if __name__ == "__main__":
    main()
