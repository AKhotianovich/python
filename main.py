import os.path


def task_1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    c = []
    for elem in range(len(a)):
        if a[elem] > 5:
            c.append(a[elem])
    print(c)


def task_2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
    print(c)


def task_3():
    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    list_key = list(a.keys())
    list_key.sort()
    for key in list_key:
        print(key, ':', a[key])


def task_4():
    a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    b = {'e': 5, 'f': 6, 'g': 7}
    for value in a:
        b[value] = a[value]
    print(b)


def task_5():
    my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    list_value = list(my_dict.values())
    list_value.sort()
    for i in range(1, 4):
        for k, v in my_dict.items():
            if v == list_value[i]:
                print(list_value[i], ':', k) #колхоз пизда, понимаю))))
                                             #Вот посмотришь код и скажешь, что нужно учить)


def task_6():
    a = ("John", "Charles", "Mike")
    b = ("Jenny", "Christy", "Monica", "Vicky")

    x = zip(a, b)
    print(set(x))


def task_7(n):
    hight = [1]
    y = [0]
    for i in range(max(n, 0)):
        print(hight)
        hight = [left + right for left, right in zip(hight + y, y + hight)]


def task_8(word):
    word1 = word[::-1]
    if word1 == word:
        print("Yes")
    else:
        print("No")


def task_9(second):

    days = second // (24 * 3600)
    second %= 24 * 3600
    hours = second // 3600
    second %= 3600
    minutes = second // 60
    second %= 60
    print(days, ":", hours, ":", minutes, ":", second)


def task_10(str):
    a = str.split(",")
    my_list = []
    my_tuple = tuple(a)
    for value in a:
        my_list.append(value)
    print(my_list, " - list")
    print(my_tuple, " - tuple")


def task_11():
    my_list = ['first', '1', '2', '3', 'last']
    print(my_list[0], ', ', my_list[len(my_list) - 1])


def task_12():
    print("hui")


def task_13(n1):
    n = n1
    for value in range(1, 3):
        n += n1 * 10**value + n
    print(n)

def task_14():
    my_list = (1, 2, 4, 8, 9, 237, 2)
    for value in my_list:
        if value == 237:
            break
        elif value % 2 == 0:
            print(value)


def task_15():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = set(a) - set(b)
    print(c)


def task_16():

    print("hui")
    print(os.listdir(path="/home/alexander"))


def task_17(n):
    n = str(n)
    sum = 0
    for value in n:
        sum += int(value)
    print(sum)


def task_18(n):
    my_text = "Бородин тупая шлюха, мать его шлюха, у него нет друзей, потому что он шлюха. Ебаная шлюха"
    my_text = my_text.replace(',', '')
    my_text = my_text.replace('.', '')
    a = my_text.split(" ")
    count = 0
    count1 = 0
    for value in a:
        if value == n:
            count += 1
    print(count)

    for i in my_text:
        if i == 'а':
            count1 += 1
    print(count1)

def task_19():
    a = "Бородин"
    b = "Шлюха"
    print(a)
    print(b)
    c = a
    a = b
    b = c
    print(a)
    print(b)


def task_20():
    mas = [15, 2, 3, 5, 30, 60, 40, 45]
    result = list(map(lambda x: not x % 15, mas))
    print(mas)
    print(result)

def task_21(n):
    if len(set(n)) == len(n):
        print("Yes")
    else:
        print("No")
    print(set(n))


def task_22():
    my_text = "Бородин тупая шлюха, мать его шлюха, у него нет друзей, потому что он шлюха. Ебаная шлюха"
    my_text = my_text.replace(',', '')
    my_text = my_text.replace('.', '')
    a = my_text.split(" ")
    max_count = 0
    new_word = ''
    for word in a:
        k = 0
        for word1 in a:
            if word == word1:
                k += 1
        if max_count < k:
            max_count = k
            new_word = word
    print(new_word)
    max_word = ''
    for i in a:
        if len(i) > len(max_word):
            max_word = i
    print(max_word)



#task_1()  # Выведите все элементы, которые меньше 5.

#task_2()  #Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

#task_3()  #Отсортируйте словарь по значению в порядке возрастания и убывания.

#task_4()  #Напишите программу для слияния нескольких словарей в один.

#task_5()  #Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

#task_6()  #Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.

#task_7(8) #Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы,
           #а каждое число внутри равно сумме двух расположенных над ним чисел.

#task_8("шалаш")  #Напишите проверку на то, является ли строка палиндромом.

#task_9(100000)  #Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

#task_10("1,2,4,5,56,7")  #Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

#task_11()  #Выведите первый и последний элемент списка.

#task_12()  #Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.

#task_13(2)  #При заданном целом числе n посчитайте n + nn + nnn.

#task_14()  #Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

#task_15()  #Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

task_16()  #Выведите список файлов в указанной директории.

#task_17(12412)  #Сложите цифры целого числа.

#task_18("шлюха")  #Посчитайте, сколько раз символ встречается в строке.

#task_19()  #Поменяйте значения переменных местами.

#task_20()  #С помощью анонимной функции извлеките из списка числа, делимые на 15.

#task_21("123675")  #Нужно проверить, все ли числа в последовательности уникальны.

#task_22()  #Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.

