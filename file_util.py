import os
import shutil
from io import StringIO

from docx import Document
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def read_pdf(filepath):
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(filepath, "rb") as fp:
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
    text = sio.getvalue()
    device.close()
    sio.close()
    return text


def search_keywords_in_files(first_name: str, last_name: str, student_id: int) -> None:
    current_dir = os.getcwd()
    keywords = {"sustainability": "SCH", "essay": "ENG", "matrix": "MATH"}
    for file in os.listdir(current_dir):
        if not file.endswith(".pdf") and not (
            file.endswith(".docx") or file.endswith(".doc")
        ):
            continue
        text = get_file_content(file)
        text = text.lower()
        for keyword, folder_name in keywords.items():
            if keyword in text:
                folders = move_to_folder_with_name(file, folder_name)
                rename_files_in_folder(folders, first_name, last_name, student_id)


def get_file_content(file):
    if file.endswith(".pdf"):
        return read_pdf(file)
    elif file.endswith(".docx") or file.endswith(".doc"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])


def move_to_folder_with_name(file: str, folder_name: str) -> list:
    current_dir = os.getcwd()
    moved_to_folders = []
    for folder in os.listdir(current_dir):
        if folder_name in folder:
            destination = os.path.join(current_dir, folder, file)
            shutil.move(file, destination)
            moved_to_folders.append(folder)
    return moved_to_folders


def rename_files_in_folder(
    folders: list, first_name: str, last_name: str, student_id: int
) -> None:
    current_dir = os.getcwd()
    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if not os.path.isdir(file):
                    original_file_name, file_extension = os.path.splitext(file)
                    new_file_name = f"{first_name.strip()} {last_name.strip()} - {student_id}{file_extension}"
                    os.rename(
                        os.path.join(folder_path, file),
                        os.path.join(folder_path, new_file_name),
                    )
