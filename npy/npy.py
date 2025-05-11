import numpy as np


# Создание из списка (ручной способ)
# a = np.array([1, 2, 3])
# b = np.array([[1, 2, 3], [4, 5, 6]])


# Специальные массивы
# np.zeros() — массив из нулей
# c = np.zeros(5)
# v = np.zeros((2, 3))


# np.ones() — массив из единиц
# print(np.ones(5))


# np.full() — массив с заданным значением

# print(np.full((2, 2), 7))


#  3. Диапазоны чисел
# np.arange() — как range(), но возвращает массив

# print(np.arange(0, 10, 2))

# np.linspace() — равномерное распределение
# print(np.linspace(0, 1, 5))


#  4. Случайные массивы

# print(np.random.rand(3))  # 1D массив из 3 случайных чисел
# print(np.random.randint(1, 10, size=(2, 2)))  # массив 2x2 из целых от 1 до 9


# a = np.arange(1, 11)
# c = np.full((3, 3), 5)
# b = np.linspace(0, 3, 7)
# print(f"a - {a.shape}{a.dtype}, c - {c.shape}{c.dtype}, b - {b.shape}{b.dtype}")

# b = np.array([[1, 2, 3], [4, 5, 6]])

# print(np.full_like(b, 5))

# Размерность (ndim)

# print(a.ndim)
# print(c.ndim)
# print(b.ndim)


# x = np.random.randint(0, 10, size=(3, 4, 2))
# print(f"ndim - {x.ndim}, shape - {x.shape}, dtype - {x.dtype}")


# a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# print(a[2])
# print(a[:, 2])
# print(a[0:2, 1:])


# reshape() — изменение формы массива
# Изменяет форму без изменения данных.
# a = np.array([1, 2, 3, 4, 5, 6])
# b = a.reshape((2, 3))
# c = b.reshape((6, 1))
# print(a)
# print(b)
# print(c)


#  2. flatten() — сглаживает (делает 1D копию массива)
# b = np.array([[1, 2], [3, 4]])
# flat = b.flatten()
# print(b)
# print(flat)


#  ravel() — сглаживает массив, но возвращает представление (view)
# b = np.array([[1, 2], [3, 4]])
# c = b.ravel()
# c[0] = 100
# print(b)


# x = np.array([[1, 2, 3], [4, 5, 6]])
# resh_x = x.reshape((3, 2))
# new_x = resh_x.flatten()
# x_ravel = resh_x.ravel()
# x_ravel[0] = 50
# print(f"x_ravel - {x_ravel}\n\n ")
# print(f"x - {x}\n\n ")
# print(f"resh_x - {resh_x}\n\n ")
# print(f"new_x - {new_x}\n\n ")


# 1. Арифметика над массивами
# NumPy позволяет выполнять векторные операции (элемент к элементу), без циклов:

# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])

# print(a + b)  # [11 22 33]
# print(b - a)  # [9 18 27]
# print(a * b)  # [10 40 90]
# print(b / a)  # [10. 10. 10.]
# print(a**2)  # [1 4 9]


# Broadcasting (трансляция)
# Позволяет выполнять операции с массивами разных форм, если они совместимы.

# Пример 1: Складываем массив и число

# a = np.array([1, 2, 3])
# print(a + 10)  # [11 12 13]


# Пример 2: Складываем массив (3×1) с (1×3)
# a = np.array([[1], [2], [3]])   форма (3, 1)
# b = np.array([10, 20, 30])   форма (3,)

# Broadcasting приводит их к общей форме (3, 3)
# print(a + b)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]


# Логические операции и маски
# Работают поэлементно и возвращают булев массив:

# a = np.array([1, 2, 3, 4, 5])
# mask = a > 2  # [False False  True  True  True]
# print(a[mask])  # [3 4 5] — только элементы > 2


# Комбинирование условий:
# a = np.array([1, 2, 3, 4, 5])
# print(a[(a > 1) & (a < 5)])  # [2 3 4]
# print(a[(a == 1) | (a == 5)])  # [1 5]

# a = np.arange(1, 11)
# new_a = a**2
# filt = new_a[new_a > 30]

# print(new_a)
# print(filt)
# print(filt + 100)


# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.repeat(b, 3, axis=0))


# arr = np.ones((5, 5))
# print(arr)
# arr[1:-1, 1:-1] = np.zeros((3, 3))
# arr[2, 2] = 9
# print(arr)


# a = np.array([4, 5, 6])
# b = np.array([1, 2, 3])
# print(np.vstack([b, a]))

# h1 = np.ones((2, 4))
# h2 = np.zeros((2, 2))
# print(h1)
# print(h2)
# print(np.hstack([h1, h2]))

a = np.arange(1, 31)
b = a.reshape(6, 5)

print(b[2:4, 0:2])
print(b[[0, 1, 2, 3], [1, 2, 3, 4]])
print(b[[0, -2, -1], -2:])
