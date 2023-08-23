import os 

current_dir = os.path.abspath(os.path.dirname("lesson2_step7.py"))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

print(os.getcwd())
print(os.path.abspath("lesson2_step7.py"))
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname("lesson2_step7.py")))