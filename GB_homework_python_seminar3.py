'''
Домашняя работа после Семинара 3
Задача 1.
Задайте список из нескольких чисел. Напишите программу, которая 
найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

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

'''
Задача 2.
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
Если остается 1 элемент без пары - умножаем его самого на себя.

Пример:

[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
'''

'''
print("Напишим программу, которая найдёт произведение пар чисел списка")
list_input = list(map(int, input(
                  "Введите через пробел список из целых чисел:\n"
                 ).split()))

def product_pairs_numbers(arg_list_input):
    count = (len(arg_list_input) + 1) // 2
    result_list = []
    for i in range(count):
        result_list.append(arg_list_input[i] * arg_list_input[-(i + 1)])
    return result_list

result = product_pairs_numbers(list_input)
print("Ответ: {}".format(result))
'''

'''
Задача 3.
Задайте список из вещественных чисел. Напишите программу, которая 
найдёт разницу между максимальным и минимальным значением дробной 
части элементов.

Пример:

[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

print("Найдём разницу между максимальным и минимальным значением "
      "дробной части элементов")
list_input = [1.1, 1.2, 3.1, 5, 10.01]
print(f"Заданный список: {list_input}")

def finding_difference(arg_list):
    min_elem = arg_list[0] * 100 % 100
    max_elem = arg_list[0] * 100 % 100
    for i in range(1, len(arg_list)):
        if (arg_list[i] * 100 % 100) != 0 and (
            arg_list[i] * 100 % 100) < min_elem:
            min_elem = arg_list[i] * 100 % 100
        elif (arg_list[i] * 100 % 100) != 0 and (
              arg_list[i] * 100 % 100) > max_elem:
            max_elem = arg_list[i] * 100 % 100
    result = (max_elem - min_elem) / 100
    print(f"Максимум: {max_elem / 100}, минимум: {min_elem / 100}")
    return result

result_difference = finding_difference(list_input)
print(f"Ответ: {result_difference}")
