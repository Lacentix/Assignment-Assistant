import os


def create_subject_folders(subject_names):
    for subject_name in subject_names:
        if not os.path.exists(subject_name):
            os.makedirs(subject_name)


def create_gitignore(subject_names):
    # Ignore created folders
    ignore_statements = (
        ["# Ignore subject folders", "*", "!.gitignore"]
        + ["!" + subject_name + "/" for subject_name in subject_names]
        + ["*/"]
    )

    # Append ignore statements to the end of the file
    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write("\n" + "\n".join(ignore_statements))
