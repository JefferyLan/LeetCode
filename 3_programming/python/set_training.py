def set_training():
    # 使用场景： 找出重复元素， 否则需要for循环挨个找
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    print(some_list)
    duplicates = set([x for x in some_list if some_list.count(x) > 1])
    print(duplicates)
    # 使用场景： 去除重复元素
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    print(some_list)
    duplicates = set([x for x in some_list if some_list.count(x) == 1])
    print(sorted(duplicates))
    # 交集，找2个集合交集（共同元素）
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print(input_set.intersection(valid))
    # 差集，找2个集合差集（不同元素），用于过滤无效数据
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print(input_set.difference(valid))






if __name__ == '__main__':
    set_training()