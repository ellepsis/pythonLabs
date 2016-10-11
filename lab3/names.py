import sys
import lxml.html


def read_file(filename):
    data = None
    file = None
    try:
        file = open(filename, 'r')
    except Exception:
        raise Exception("Can't open file :" + filename)
    try:
        data = file.read()
    except Exception:
        raise Exception("Can't read file : " + filename)
    return data


def extr_name(filename : str):
    """
  Вход: nameYYYY.html, Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
  '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
  """
    rows = None
    f_data_list = list()
    m_data_list = list()
    page = None
    year = int(filename[4:8])
    read_data = read_file(filename)
    try:
        page = lxml.html.fromstring(read_data)
    except Exception:
        print("Can't parse html ")
    try:
        rows = page.xpath('//tr[@align="right"]/td/..')
    except Exception:
        print("Can't find data")
    for row in rows:
        row_data = row.getchildren()
        f_data = (row_data[2].text, int(row_data[0].text))
        m_data = (row_data[1].text, int(row_data[0].text))
        f_data_list.append(f_data)
        m_data_list.append(m_data)
    f_data_list = sorted(f_data_list, key=lambda x: x[0])
    m_data_list = sorted(m_data_list, key=lambda x: x[0])
    return m_data_list, f_data_list, year


# all_file_res is ->
# list contains result from all files of ->
# cartage contains male and female in specified order of->
# list of couple that contains name and position, which must be sorted by position asc
def print_top_names(count, all_file_res):
    f_res_list = list()
    m_res_list = list()
    sorted_list = list()
    for i in all_file_res:
        male = sorted(i[0], key=lambda x: x[1])
        female = sorted(i[1], key=lambda x: x[1])
        sorted_list.append((male,female))
    for i in range(count-1):
        for v in sorted_list:
            if len(f_res_list) < count and v[1][i][0] not in f_res_list:
                f_res_list.append(v[1][i][0])
            if len(m_res_list) < count and v[0][i][0] not in m_res_list:
                m_res_list.append(v[0][i][0])
    print("\nTop " + str(count) + " male names")
    for e in m_res_list:
        print(e)
    print("\nTop " + str(count) + " female names")
    for e in f_res_list:
        print(e)


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    all_file_res = list()
    for arg in args:
        res = None
        try:
            res = extr_name(arg)
            all_file_res.append(res)
        except Exception as e:
            print(e)
        print("\nMale names in year " + str(res[2]))
        for v in res[0]:
            print(v)
        print("\nFemale names in year " + str(res[2]))
        for v in res[1]:
            print(v)
    print_top_names(10, all_file_res)
    return



    # для каждого переданного аргументом имени файла, вывести имена  extr_name

    # напечатать ТОП-10 муж и жен имен из всех переданных файлов


if __name__ == '__main__':
    main()
