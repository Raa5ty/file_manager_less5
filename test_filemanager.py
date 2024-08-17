'''
В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера

В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина

(Дополнительно*) так же попробовать написать тесты для ""грязных"" функций, например копирования файла/папки.
'''

import os
import shutil
import pytest
from unittest.mock import patch
from main import create_folder, delete_item, copy_item, list_directory, list_folders, list_files, os_info, creator_info
from quiz import quiz
from bank_account import bank_account
from io import StringIO

@pytest.fixture
def setup_and_teardown():
    # Создание временного каталога для тестов
    if not os.path.exists('test_dir'):
        os.makedirs('test_dir')
    yield
    # Удаление временного каталога после тестов
    if os.path.exists('test_dir'):
        shutil.rmtree('test_dir')

def test_create_folder(setup_and_teardown):
    with patch('builtins.input', return_value='test_dir/test_folder'):
        if os.path.exists('test_dir/test_folder'):
            shutil.rmtree('test_dir/test_folder')

        create_folder()

        assert os.path.exists('test_dir/test_folder')

        shutil.rmtree('test_dir/test_folder')

def test_delete_item(setup_and_teardown):
    os.makedirs('test_dir/test_folder')

    with patch('builtins.input', return_value='test_dir/test_folder'):
        delete_item()

    assert not os.path.exists('test_dir/test_folder')

def test_copy_item(setup_and_teardown):
    os.makedirs('test_dir/test_folder')

    with patch('builtins.input', side_effect=['test_dir/test_folder', 'test_dir/copied_folder']):
        copy_item()

    assert os.path.exists('test_dir/copied_folder')

    shutil.rmtree('test_dir/test_folder')
    shutil.rmtree('test_dir/copied_folder')

def test_list_directory(setup_and_teardown):
    with patch('builtins.print') as mocked_print:
        list_directory()
        assert mocked_print.called

def test_list_folders(setup_and_teardown):
    with patch('builtins.print') as mocked_print:
        list_folders()
        assert mocked_print.called

def test_list_files(setup_and_teardown):
    with patch('builtins.print') as mocked_print:
        list_files()
        assert mocked_print.called

def test_os_info(setup_and_teardown):
    with patch('builtins.print') as mocked_print:
        os_info()
        assert mocked_print.called

def test_creator_info(setup_and_teardown):
    with patch('builtins.print') as mocked_print:
        creator_info()
        mocked_print.assert_called_with('Создатель программы: Руслан')

# Тестирование функции quiz
def test_quiz_correct_answers():
    inputs = ['1799', '1828', '1821', '1840', '1895']

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            quiz()
            output = mocked_stdout.getvalue().splitlines()

            assert "Количество правильных ответов: 5" in output
            assert "Количество ошибок: 0" in output
            assert "Процент правильных ответов: 100.0" in output
            assert "Процент неправильных ответов: 0.0" in output

def test_quiz_incorrect_answers():
    inputs = ['1800', '1830', '1830', '1850', '1900']

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            quiz()
            output = mocked_stdout.getvalue().splitlines()

            assert "Количество правильных ответов: 0" in output
            assert "Количество ошибок: 5" in output
            assert "Процент правильных ответов: 0.0" in output
            assert "Процент неправильных ответов: 100.0" in output

def test_quiz_mixed_answers():
    inputs = ['1799', '1830', '1821', '1840', '1895']

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            quiz()
            output = mocked_stdout.getvalue().splitlines()

            assert "Количество правильных ответов: 4" in output
            assert "Количество ошибок: 1" in output
            assert "Процент правильных ответов: 80.0" in output
            assert "Процент неправильных ответов: 20.0" in output

# Тестирование функции bank_account
def test_bank_account_deposit():
    inputs = ['1', '100', '4']  # Пополнение на 100 и выход

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            bank_account()
            output = mocked_stdout.getvalue().splitlines()

            assert "Счет пополнен на 100.0 руб. Текущий баланс: 100.0 руб." in output
            assert "Выход из программы." in output


def test_bank_account_purchase_success():
    inputs = ['1', '200', '2', '50', 'Книга', '3', 'Книга - 50.0 руб.', '4']

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            bank_account()
            output = mocked_stdout.getvalue().splitlines()

            assert "Счет пополнен на 200.0 руб. Текущий баланс: 200.0 руб." in output
            assert 'Покупка "Книга" на сумму 50.0 руб. выполнена. Остаток на счете: 150.0 руб.' in output
            assert 'История покупок:' in output
            assert 'Книга - 50.0 руб.' in output
            assert "Текущий баланс: 150.0 руб." in output
            assert "Выход из программы." in output

def test_bank_account_purchase_fail():
    inputs = ['1', '50', '2', '100', 'Книга', '4']  # Пополнение на 50, попытка купить на 100 и выход

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            bank_account()
            output = mocked_stdout.getvalue().splitlines()

            assert "Счет пополнен на 50.0 руб. Текущий баланс: 50.0 руб." in output
            assert "Недостаточно средств на счете." in output
            assert "Выход из программы." in output

def test_bank_account_view_history():
    inputs = ['1', '300', '2', '100', 'Книга', '2', '200', 'Тетрадь', '3', 'История покупок', '4']

    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            bank_account()
            output = mocked_stdout.getvalue().splitlines()

            assert "Счет пополнен на 300.0 руб. Текущий баланс: 300.0 руб." in output
            assert 'Покупка "Книга" на сумму 100.0 руб. выполнена. Остаток на счете: 200.0 руб.' in output
            assert 'Покупка "Тетрадь" на сумму 200.0 руб. выполнена. Остаток на счете: 0.0 руб.' in output
            assert "История покупок:" in output
            assert "Книга - 100.0 руб." in output
            assert "Тетрадь - 200.0 руб." in output
            assert "Текущий баланс: 0.0 руб." in output
            assert "Выход из программы." in output