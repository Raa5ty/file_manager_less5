import pytest
import math


# Тест для функции filter
def test_filter_even_numbers():
    nums = [1, 2, 3, 4, 5, 6]
    result = list(filter(lambda x: x % 2 == 0, nums))
    assert result == [2, 4, 6]


def test_filter_non_empty_strings():
    strings = ["hello", "", "world", "", "python"]
    result = list(filter(lambda x: x != "", strings))
    assert result == ["hello", "world", "python"]


# Тесты для функции map
def test_map_square_numbers():
    nums = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x ** 2, nums))
    assert result == [1, 4, 9, 16, 25]


def test_map_uppercase_strings():
    strings = ["hello", "world", "python"]
    result = list(map(lambda x: x.upper(), strings))
    assert result == ["HELLO", "WORLD", "PYTHON"]


# Тесты для функции sorted
def test_sorted_numbers():
    nums = [5, 2, 9, 1, 5, 6]
    result = sorted(nums)
    assert result == [1, 2, 5, 5, 6, 9]


def test_sorted_reverse():
    nums = [5, 2, 9, 1, 5, 6]
    result = sorted(nums, reverse=True)
    assert result == [9, 6, 5, 5, 2, 1]


def test_sorted_strings():
    strings = ["banana", "apple", "cherry"]
    result = sorted(strings)
    assert result == ["apple", "banana", "cherry"]


# Тесты для функций из библиотеки math

# Тест для math.pi
def test_math_pi():
    assert math.isclose(math.pi, 3.141592653589793, rel_tol=1e-9)


# Тест для math.sqrt
def test_math_sqrt():
    assert math.sqrt(16) == 4
    assert math.sqrt(0) == 0
    assert math.isclose(math.sqrt(2), 1.414213562, rel_tol=1e-9)


# Тест для math с использованием цикла for
def test_math_sqrt():
    for i in range(2, 11, 2):
        expected_result = i ** 0.5
        assert math.isclose(math.sqrt(i), expected_result, rel_tol=1e-9)

    # Также проверим нулевое значение
    assert math.sqrt(0) == 0


# Тест для math.pow
def test_math_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(4, 0.5) == 2
    assert math.isclose(math.pow(2, -3), 0.125, rel_tol=1e-9)


def test_math_pow():
    # Проверяем возведение чисел в положительные степени
    for x in range(1, 6):  # x от 1 до 5
        for y in range(1, 4):  # y от 1 до 3
            expected_result = x ** y
            assert math.pow(x, y) == expected_result

    # Проверяем возведение в нулевую степень
    for x in range(1, 6):
        assert math.pow(x, 0) == 1

    # Проверяем возведение в отрицательную степень
    for x in range(1, 6):
        for y in range(-1, -4, -1):  # y от -1 до -3 (отрицательные степени)
            expected_result = x ** y
            assert math.isclose(math.pow(x, y), expected_result, rel_tol=1e-9)


# Тест для math.hypot
def test_math_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(5, 12) == 13
    assert math.hypot(0, 0) == 0


def test_math_hypot():
    for x in range(1, 6):  # x от 1 до 5
        for y in range(1, 6):  # y от 1 до 5
            expected_result = math.sqrt(x ** 2 + y ** 2)
            assert math.isclose(math.hypot(x, y), expected_result, rel_tol=1e-9)

    # Проверим случай, когда один из катетов равен нулю
    for x in range(1, 6):
        assert math.hypot(x, 0) == x
        assert math.hypot(0, x) == x

    # Проверим случай, когда оба катета равны нулю
    assert math.hypot(0, 0) == 0