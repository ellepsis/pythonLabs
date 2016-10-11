from heapq import merge


# 1.
# Вх: список чисел, Возвр: список чисел, где
# повторяющиеся числа урезаны до одного
# пример [0, 2, 2, 3] returns [0, 2, 3].
def rm_adj(nums):
    return list(set(nums))


# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список 
def f2(list1, list2):
    return list(merge(list1, list2))


def test():
    is_err = False
    if rm_adj([0, 2, 2, 3]) != [0, 2, 3]:
        print("Error in rm_adj")
        is_err = True
    if f2([0, 2, 2, 3, 6], [1, 2, 5]) != [0, 1, 2, 2, 2, 3, 5, 6]:
        print("Error in f2")
        is_err = True
    if not is_err:
        print("All tests passed successfully")


def main():
    test()
    print("rm_adj([0, 2, 2, 3]) -> " + str(rm_adj([0, 2, 2, 3])))
    print("f2([0, 2, 2, 3, 6], [1, 2, 5]) -> " + str(f2([0, 2, 2, 3, 6], [1, 2, 5])))


if __name__ == '__main__':
    main()
