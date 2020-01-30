
def multipy(x):
    return x**2
def format_name(x):
    return x[0:1].upper() + x[1:].lower()

def map_reduce():
    """
    test map usage
    :return:
    """
    item = range(1, 6, 1)
    #使用lambda匿名函数直接定义函数体
    squared = map(lambda x: x**2, item)
    print(list(item))
    print(list(squared))
    # 使用函数,输入只有单个数组
    squared = map(multipy, item)
    print(list(squared))
    # 用于清理数据，姓名首字母大写，其他小写
    name_list = ['adam', 'LISA', 'barT']
    formatted_name = map(format_name, name_list)
    print(list(formatted_name))
    #   使用lambda匿名函数,输入多个数组，可计算矩阵按列算（并行）
    squared = map(lambda x, y, z: x + y + z, item, item, item)
    print(list(squared))
    #   使用lambda匿名函数,输入多个数组，可计算矩阵按列算（并行）
    squared = map(lambda x, y, z: (x * y * z, x + y + z), item, item, item)
    print(list(squared))
    # 特殊用法， 类型转换
    string = '12344566'
    int_iter = map(int, string)
    print(list(int_iter))
    # 如果函数为None, 自动假定一个‘identity'函数,这时候就是模仿 zip()函数
    # 但是在 python3中，返回是一个迭代器，所以它其实是不可调用的
    zipped = map(None, item, item)
    #print(list(zipped))
    zipped = zip(item, item)
    print(list(zipped))
    #提取字典中的key，并将结果放在一个list中：
    dict = {1: 2, 2: 3, 3: 4}
    dict_key = map(int, dict)
    print(list(dict_key))
    # 使用 lambda函数来排序，按照每个元组第一维数据排序
    tuple_items = [(1, 2), (4, 1), (9, 10), (13, -3)]
    tuple_items.sort(key=lambda x: x[1])
    print(tuple_items)
    # 验证zip 和unzip， 列表并⾏排序
    data = list(zip(range(6, 1, -1), range(1, 6, 1)))
    print("zip two lists and convert to a list with tuple elements: {}".format(data))
    data.sort()
    print("sorted list: {}".format(data))
    unzip_list1, unzip_list2 = list(zip(*data))
    print(unzip_list1, unzip_list2)
    list1 = list(map(lambda t: list(t), zip(*data)))
    print(list1)



if __name__ == '__main__':
    map_reduce()

