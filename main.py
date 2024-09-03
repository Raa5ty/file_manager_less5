import os
import shutil
import platform
from quiz import quiz
from bank_account import bank_account
from decorator import decorator_func

# В этой функции мы использовали тернарный оператор дважды, для создания папки и для вывода сообщения:
def create_folder():
    folder_name = input('Введите название папки: ')
    os.makedirs(folder_name) if not os.path.exists(folder_name) else None
    print(f'Папка {folder_name} {"создана" if not os.path.exists(folder_name) else "уже существует"}.')

# Старый вариант функции для сравнения:
# def create_folder():
#     folder_name = input('Введите название папки: ')
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#         print(f'Папка {folder_name} создана.')
#     else:
#         print(f'Папка {folder_name} уже существует.')

# В этой функции мы использовали тернарный оператор
def delete_item():
    item_name = input('Введите название файла или папки: ')
    if os.path.exists(item_name):
        shutil.rmtree(item_name) if os.path.isdir(item_name) else os.remove(item_name)
        print(f'{"Папка" if os.path.isdir(item_name) else "Файл"} {item_name} удален{"а" if os.path.isdir(item_name) else ""}.')
    else:
        print(f'Файл или папка {item_name} не найдены.')

# Старый вариант функции для сравнения:
# def delete_item():
#     item_name = input('Введите название файла или папки: ')
#     if os.path.exists(item_name):
#         if os.path.isdir(item_name):
#             shutil.rmtree(item_name)
#             print(f'Папка {item_name} удалена.')
#         else:
#             os.remove(item_name)
#             print(f'Файл {item_name} удален.')
#     else:
#         print(f'Файл или папка {item_name} не найдены.')

# В этой функции мы использовали тернарный оператор
def copy_item():
    item_name = input('Введите название файла или папки: ')
    new_item_name = input('Введите новое название файла или папки: ')
    
    if os.path.exists(item_name):
        shutil.copytree(item_name, new_item_name) if os.path.isdir(item_name) else shutil.copy2(item_name, new_item_name)
        print(f'{"Папка" if os.path.isdir(item_name) else "Файл"} {item_name} скопирован{"а" if os.path.isdir(item_name) else ""} в {new_item_name}.')
    else:
        print(f'Файл или папка {item_name} не найдены.')
# Старый вариант функции для сравнения:
# def copy_item():
#     item_name = input('Введите название файла или папки: ')
#     new_item_name = input('Введите новое название файла или папки: ')
#     if os.path.exists(item_name):
#         if os.path.isdir(item_name):
#             shutil.copytree(item_name, new_item_name)
#             print(f'Папка {item_name} скопирована в {new_item_name}.')
#         else:
#             shutil.copy2(item_name, new_item_name)
#             print(f'Файл {item_name} скопирован в {new_item_name}.')
#     else:
#         print(f'Файл или папка {item_name} не найдены.')

@decorator_func
def list_directory():
    items = os.listdir()
    print('Содержимое рабочей директории:')
    for item in items:
        print(item)

@decorator_func
def list_folders():
    items = [item for item in os.listdir() if os.path.isdir(item)]
    print('Папки в рабочей директории:')
    for item in items:
        print(item)

@decorator_func
def list_files():
    items = [item for item in os.listdir() if os.path.isfile(item)]
    print('Файлы в рабочей директории:')
    for item in items:
        print(item)

def save_directory_contents():
    files = [item for item in os.listdir() if os.path.isfile(item)]
    dirs = [item for item in os.listdir() if os.path.isdir(item)]
    
    with open('listdir.txt', 'w') as f:
        f.write('files: ' + ', '.join(files) + '\n')
        f.write('dirs: ' + ', '.join(dirs))
    
    print('Содержимое рабочей директории сохранено в файл listdir.txt')

# Добавленна обработка исключений при чтении файла:
@decorator_func
def read_saved_directory_contents():
    try:
        with open('listdir.txt', 'r') as f:
            contents = f.read()
        print("Содержимое файла listdir.txt:")
        print(contents)
    except FileNotFoundError:
        print("Файл listdir.txt не найден. Сначала сохраните содержимое рабочей директории.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        print(f"Подробности ошибки: {e}")
    return None

@decorator_func
def os_info():
    print('Информация об операционной системе:')
    print(f'Название ОС: {platform.system()}')
    print(f'Версия ОС: {platform.version()}')
    print(f'Архитектура: {platform.architecture()}')

@decorator_func
def creator_info():
    print('Создатель программы: Руслан')

def main():
    while True:
        print('\nМеню:')
        print('1. Создать папку')
        print('2. Удалить (файл/папку)')
        print('3. Копировать (файл/папку)')
        print('4. Просмотр содержимого рабочей директории')
        print('5. Посмотреть только папки')
        print('6. Посмотреть только файлы')
        print('7. Просмотр информации об операционной системе')
        print('8. Создатель программы')
        print('9. Играть в викторину')
        print('10. Мой банковский счет')
        print('11. Сохранить содержимое рабочей директории в файл')
        print('12. Прочитать файл с сохранённой рабочей директорией')
        print('13. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            create_folder()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            copy_item()
        elif choice == '4':
            list_directory()
        elif choice == '5':
            list_folders()
        elif choice == '6':
            list_files()
        elif choice == '7':
            os_info()
        elif choice == '8':
            creator_info()
        elif choice == '9':
            quiz()
        elif choice == '10':
            bank_account()
        elif choice == '11':
            save_directory_contents()
        elif choice == '12':
            read_saved_directory_contents()
        elif choice == '13':
            print('Выход из программы...')
            break
        else:
            print('Неверный выбор. Попробуйте снова.')

if __name__ == '__main__':
    main()
