import tkinter as tk
import os
from tkinter import filedialog

# Функция для выбора файла
def select_file():
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно tkinter
    file_path = filedialog.askopenfilename(title="Выберите файл new_proxy.txt", filetypes=[("Текстовые файлы", "*.txt")])
    return file_path

file_path = select_file()

if not file_path:
    print("Файл не выбран.")
    exit()
    
with open(file_path, "r", newline='') as file:
    lines = file.readlines()

ip_addresses = []
login = ""
password = ""
port = ""

for line in lines:
    line = line.strip()
    if line.startswith("Логин:"):
        login = line.split(":")[1].strip()
    elif line.startswith("Пароль:"):
        password = line.split(":")[1].strip()
    elif line.startswith("Порт HTTP/S-proxy:"):
        port = line.split(":")[1].strip()
    elif line:
        ip_addresses.append(line)

output = ""

for ip in ip_addresses:
    output += f"{ip};{port};{login};{password};\n"

# Получаем путь к каталогу, где находится файл new_proxy.txt
directory = os.path.dirname(file_path)

# Создаем путь к файлу output.txt в этом же каталоге
output_path = os.path.join(directory, "output.txt")

# Сохраняем результат в файл output.txt в нужной директории
with open(output_path, "w") as file:
    file.write(output)

print(f"Результат сохранен в файле {output_path}")
