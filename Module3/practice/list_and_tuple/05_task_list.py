# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

# TODO: your code here

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.    киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
lngth_fruit = []
for fruit in fruits:
    lngth_fruit.append(len(fruit))
    print(lngth_fruit)

mx_lngth_fruit = max(lngth_fruit)

i = 1
for fr in fruits:
    print(f"{i}. {fr:>{mx_lngth_fruit}}")
    i += 1
