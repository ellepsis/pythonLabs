# 1.
# Входящие параметры: int <count> , 
# Результат: string в форме
# "Number of: <count>", где <count> число из вход.парам.
#  Если число равно 10 или более, напечатать "many"
#  вместо <count>
#  Пример: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'

def num_of_items(count):
    return "Number of: " + ("many" if count > 10 else str(count))


# 2. 
# Входящие параметры: string s, 
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
    if len(s) < 2:
        raise Exception("string length must be bigger than 1 symbol")
    return s[0] + s[1] + s[-2] + s[-1]


# 3.
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
# s.replace(stra, strb) 

def replace_char(s):
    sym = s[0]
    s = s.replace(sym, "*")
    return sym+s[1:]


# 4
# Входящие параметры: string a и b, 
# Результат: string где <a> и <b> разделены пробелом 
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    return a + ' ' + b


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(res, expt):
    return res == expt

def main():
    has_err = False
    if not test(num_of_items(213), 'Number of: many'):
        print("error in num_of_items")
        has_err = True
    if not test(num_of_items(6), 'Number of: 6'):
        print("error in num_of_items")
        has_err = True
    if not test(start_end_symbols("welcome"), "weme"):
        print("error in start_end_symbols")
        has_err = True
    if not test(replace_char("bibble"), 'bi**le'):
        print("error in replace_char")
        has_err = True
    if not test(str_mix('max', 'pid'), 'max pid'):
        print("error in str_mix")
        has_err = True
    if not has_err:
        print("Tests passed successfully")
    has_err = True

    print("num_of_items(123) -> " + num_of_items(123))
    print("num_of_items(6) -> " + num_of_items(6))
    print('start_end_symbols("welcome") -> ' + start_end_symbols("welcome"))
    print('replace_char("bibble") -> ' + replace_char("bibble"))
    print("str_mix('max', 'pid') -> " + str_mix('max', 'pid'))

if __name__ == '__main__':
    main()
