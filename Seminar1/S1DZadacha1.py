# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input("Введите номер дня недели: "))

if 5 < n < 8:
    print("Да, выходной")
elif n >= 8:
    print("Введен неправильный номер дня недели")
else:
    print("Нет, будний")