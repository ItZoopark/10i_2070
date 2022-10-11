from random import randint
# структуры данных (список)
numbers = [2, 12, 234, 456, 3432, 9708]
print(numbers)
print(type(numbers))
print(numbers[0])
print(numbers[1])
print(numbers[2])
# len - length
numbers_size = len(numbers)
last_index = numbers_size - 1
print(numbers[last_index])
print(numbers[-1])
# генерация списка значениями
# первый способ
x_range = list(range(100))
print(x_range)
# второй способ
y = [0] * 10
print(y)
# списочное выражение - list comprehension
a = [(i+2)/3 for i in range(10)]
print(a)
# генерация списка рандомными числами
b = [randint(0, 10) for i in range(30)]
print(b)
# добавление элементов в список
a = [12, 3, 5, 6]
a.append(1000) # добавление в конец
print(a)
a.insert(2, 2000)
print(a)
a[0] = 3000
print(a)