import re
import string1

# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing",
# если в конце нет уже "ing", иначе добавить "ly".
def v(s):
    if len(s) > 3:
        return s + ("ly" if s[-3:] == "ing" else "ing")
    return s


# 2. 
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!

def nb(s):
    return re.sub("not.*bad", "good", s)

def main():
    has_err = False
    if not string1.test(v("qw"), "qw"):
        print("error in 1")
        has_err = True
    if not string1.test(v("asdf"), "asdfing"):
        print("error in 2")
        has_err = True
    if not string1.test(v("asdfing"), "asdfingly"):
        print("error in 3")
        has_err = True
    if not string1.test(nb("This music is not so bad!"), 'This music is good!'):
        print("error in 4")
        has_err = True
    if not has_err:
        print("tests passed successfully")

    print('v("qw") -> ' + v("qw"))
    print('v("asdf") -> ' + v("asdf"))
    print('v("asdfing") -> ' + v("asdfing"))
    print('nb("This music is not so bad!") -> ' + nb("This music is not so bad!"))

if __name__ == '__main__':
    main()
