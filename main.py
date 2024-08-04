import os
import shutil
import platform
from quiz import quiz
from bank_account import bank_account

def create_folder():
    folder_name = input('Введите название папки: ')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f'Папка {folder_name} создана.')
    else:
        print(f'Папка {folder_name} уже существует.')

def delete_item():
    item_name = input('Введите название файла или папки: ')
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            shutil.rmtree(item_name)
            print(f'Папка {item_name} удалена.')
        else:
            os.remove(item_name)
            print(f'Файл {item_name} удален.')
    else:
        print(f'Файл или папка {item_name} не найдены.')

def copy_item():
    item_name = input('Введите название файла или папки: ')
    new_item_name = input('Введите новое название файла или папки: ')
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            shutil.copytree(item_name, new_item_name)
            print(f'Папка {item_name} скопирована в {new_item_name}.')
        else:
            shutil.copy2(item_name, new_item_name)
            print(f'Файл {item_name} скопирован в {new_item_name}.')
    else:
        print(f'Файл или папка {item_name} не найдены.')

def list_directory():
    items = os.listdir()
    print('Содержимое рабочей директории:')
    for item in items:
        print(item)

def list_folders():
    items = [item for item in os.listdir() if os.path.isdir(item)]
    print('Папки в рабочей директории:')
    for item in items:
        print(item)

def list_files():
    items = [item for item in os.listdir() if os.path.isfile(item)]
    print('Файлы в рабочей директории:')
    for item in items:
        print(item)

def os_info():
    print('Информация об операционной системе:')
    print(f'Название ОС: {platform.system()}')
    print(f'Версия ОС: {platform.version()}')
    print(f'Архитектура: {platform.architecture()}')

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
        print('11. Выход')

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
            print('Выход из программы...')
            break
        else:
            print('Неверный выбор. Попробуйте снова.')

if __name__ == '__main__':
    main()
