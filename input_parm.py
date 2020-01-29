def test_var_args(f_arg, *argv, **kwargs):
    print("f_arg={}".format( f_arg))
    for arg in argv:
        print("argv: {}".format(arg))
    for key, value in kwargs.items():
        print("{}={}".format(key, value))


if __name__ == '__main__':
    test_var_args('JefferyLan', 'argv1', 'argv2', 'argv3', name="JefferyLan", dob='1981-08-13', gender="male" )

