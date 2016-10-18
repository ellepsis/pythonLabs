"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...] 

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим 
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach


"""

import random
import re
import sys


def read_file(filename: str):
    try:
        file = open(filename, "r")
        res = file.read()
        return res
    except Exception:
        raise Exception("Can't read file")


def mem_dict(filename: str):
    file_content = read_file(filename)
    words = list(map(lambda x: x.lower(), re.findall(r"[\w']+", file_content)))
    word_dict = {"": words, words[len(words) - 1]: [""]}
    for i in range(0, len(words) - 1):
        if word_dict.get(words[i]) is None:
            word_dict[words[i]] = [words[i + 1]]
        else:
            word_dict.get(words[i]).append(words[i + 1])
    word = ""
    res = ""
    for i in range(0, len(words) - 1):
        dict_arr = word_dict[word]
        res = res + ' ' + word
        word = dict_arr[random.randint(0, len(dict_arr) - 1) if len(dict_arr) > 1 else 0]
    print(res)


def main(argv):
    if len(argv) != 1:
        print('Filename argument is missing. Usage: ./script.py filename')
        sys.exit(1)
    mem_dict(argv[0])
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])
