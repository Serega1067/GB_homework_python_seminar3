'''
Домашняя работа после Семинара 3
Задача 1.
Задайте список из нескольких чисел. Напишите программу, которая 
найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

print("Найдём сумму элементов списка стоящих на нечётной позиции")
list_a = list(map(int, input(
              "Введите элементы списка, как целые числа разделённые " +
              "пробелом\n"
              ).split(" ")))

result = 0
print("Элементы списка стоящие на нечётных позициях: ", end="")
for i in range(len(list_a)):
    if i % 2 != 0:
        print(list_a[i], end=" ")
        result += list_a[i]
print()

print(f"Ответ: {result}")

'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Если остается 1 элемент без пары - умножаем его самого на себя.

Пример:

[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''