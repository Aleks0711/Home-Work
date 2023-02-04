import pathlib
import shutil

file_path = ('C\\Users\\alex2\\PycharmProjects\\026\\folder2\\2_2.py')
def return_file(file_path):
    file_name = pathlib.Path(file_path).name
    shutil.copy(file_path, './' + file_name)
print('2_2.py возвращен в папку с 2.py')


# Вывод
#2_2.py возвращен в папку с 2.py
