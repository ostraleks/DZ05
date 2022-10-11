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
# def words(number):
#     text = ""
#     for i in range(number):
#         text += "".join([random.choice("абв") for i in range (3)]) + " "
#     return text
# a = int(input("Введите количество слов "))
# if a > 0:
#     print(words(a))
#     print(words(a).replace("абв ", ""))
# else:
#      print("The data is incorrect")



# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

# def input(file_txt):
#     with open(file_txt, "r") as file_in:
#         stroka = file_in.readline()
#         return stroka

# def output(file_txt, code):
#     with open(file_txt, 'a') as file_out:
#         file_out.writelines(code + '\n')

# def coding(stroka):
#     k = 1
#     string = ""
#     for i in range(len(stroka)-1):
#         if stroka[i] == stroka[i+1]:
#             k += 1
#         else:
#             string += str(k)+stroka[i]
#             k = 1
#     return(string)    

# infile = "text_words.txt"
# outfile = "text_code_words.txt"

# s = input(infile)
# print(s)
# st = coding(s)
# print(st)
# output(outfile, st)  


# line_count = sum(1 for line in open('text_words.txt'))
# print(line_count)
# n = 0
# while n < line_count:
#     # with open('text_words.txt', "r") as file_in:
#     #     stroka = file_in.readline()
#     stroka = open ("text_words.txt", "r"). readlines () [n]
#     print(stroka)
#     k = 1
#     prev_symbol = ""
#     string = ""
#     print(len(stroka))
#     for symbol in stroka:
#         if symbol != prev_symbol:
#             if prev_symbol:
#                 string += str(k) + prev_symbol
#             k = 1
#             prev_symbol = symbol
#         else:
#             k += 1
#             print(string)
#     with open('text_code_words.txt', 'a') as file_out:
#         file_out.writelines(string + '\n')
#     n +=1



import os.path
# if os.path.exists("text_words.txt") and not os.path.exists('text_code_words.txt'):
def code(text_words = "text_words.txt", code_text = "text_code_words.txt"):
    if os.path.exists(text_words) and not os.path.exists(code_text):
        for stroka in open (text_words, "r"). readlines ():
            print(stroka)
            count = 1
            prev_symbol = ""
            string = ""
            for symbol in stroka:
                if symbol != prev_symbol:
                    if prev_symbol:
                        string += str(count) + prev_symbol
                    count = 1
                    prev_symbol = symbol
                else:
                    count += 1
            print(string)
            with open(code_text, 'a') as file_out:
                file_out.writelines(string + '\n')
    else:
        print("The files do not exist in the system!")
def decode(code_text="text_code_words.txt"):
    if os.path.exists(code_text):
        for stroka in open (code_text, "r"):
            decode = ''
            count = ''
            for char in stroka:
                if char == chr(10):
                    break
                elif char.isdigit():
                    count += char
                else:
                    print("count= ", count)
                    decode += char * int(count)
                    count = ''
            open(code_text, "a").writelines(decode + "\n")
    else:
        print("The files do not exist in the system!")
        # with open(code_text) as my_f_1, \
        #         open(text, "a") as my_f_2:
        #     for i in my_f_1:
        #         decode = ''
        #         count = ''
        #         for char in i:
        #             if char.isdigit():
        #                 count += char
        #             else:
        #                 decode += char * int(count)
        #                 count = ''
        #         my_f_2.write(decode)
    
       

code()
decode()