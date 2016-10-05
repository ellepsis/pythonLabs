

# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему
def me(words):
    count = 0
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            count += 1
    return count


# 2.
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
    list_x = []
    list_non_x = []
    for word in words:
        if word.startswith('x'):
            list_x.append(word)
        else:
            list_non_x.append(word)
    list_non_x.sort()
    list_x.sort()
    list_x.extend(list_non_x)
    return list_x


# 3.
# Вх: список непустых кортежей,
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def f3(t_list):
    t_list.sort(key=lambda x: x[len(x)-1])
    return t_list


#test(...)



#if __name__ == '__main__':
#    main()
