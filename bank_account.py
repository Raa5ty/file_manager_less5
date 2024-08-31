"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
"""
Lesson_7
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл
3. Добавить сохранение истории покупок в файл
"""
import os
import pickle

FILE_NAME = 'sum_amount.txt'
balance = 0

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'rb') as f:
        balance = pickle.load(f)

def save_balance():
    global balance
    with open(FILE_NAME, 'wb') as f:
        pickle.dump(balance, f)

HISTORY_FILE = 'purchase_history.txt'
purchases_history = {}

if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'rb') as f:
        purchases_history = pickle.load(f)

def save_purchase_history(history):
    with open(HISTORY_FILE, 'wb') as f:
        pickle.dump(history, f)


def bank_account():
    global balance
    global purchases_history

    while True:
        print('\n' + '-' * 10 + ' Программа Банковский Счёт ' + '-' * 10)
        print(f'Текущий баланс: {balance} руб.')
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            deposit_amount = float(input('Введите сумму для пополнения счета: '))
            balance += deposit_amount
            save_balance()
            print(f'Счет пополнен на {deposit_amount} руб. Текущий баланс: {balance} руб.')

        elif choice == '2':
            purchase_amount = float(input('Введите сумму покупки: '))
            if purchase_amount > balance:
                print('Недостаточно средств на счете.')
            else:
                purchase_name = input('Введите название покупки: ')
                balance -= purchase_amount
                save_balance()
                if purchase_name in purchases_history:
                    purchases_history[purchase_name] += purchase_amount
                else:
                    purchases_history[purchase_name] = purchase_amount
                save_purchase_history(purchases_history)
                print(f'Покупка "{purchase_name}" на сумму {purchase_amount} руб. выполнена. Остаток на счете: {balance} руб.')

        elif choice == '3':
            if not purchases_history:
                print('История покупок пуста.')
            else:
                print('История покупок:')
                for purchase_name, total_amount in purchases_history.items():
                    print(f'{purchase_name} - {total_amount} руб.')
                print(f'Текущий баланс: {balance} руб.')

        elif choice == '4':
            print('Выход из программы.')
            break

        else:
            print('Неверный пункт меню.')

if __name__ == "__main__":
    bank_account()

