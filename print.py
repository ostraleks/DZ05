# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

# import random
# a = int(input("Введите количество слов "))
# if a > 0:
#     text = ""
#     for i in range(a):
#         text += "".join([random.choice("абв") for i in range (3)]) + " "
#     print(text)
#     print(text.replace("абв ", ""))
# else:
#      print("The data is incorrect")
