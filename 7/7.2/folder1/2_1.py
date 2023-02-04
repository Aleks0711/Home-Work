import pathlib
import shutil

def return_file(file_path):
    # Получаем путь к файлу
    file_path = pathlib.Path('C\\Users\\alex2\\PycharmProjects\\026\\folder2\\2_2.py')
    # Получаем путь к папке, в которую необходимо скопировать файл
    dest_path = pathlib.Path('C\\Users\\alex2\\PycharmProjects\\026\\folder1')
    # Копируем файл в нужную папку
    shutil.copy(file_path, dest_path)