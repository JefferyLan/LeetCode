import time


def auth(func):
    print('this is auth')

    def inner(*args, **kwargs):
        print(f'this is a inner {args}: {kwargs}, func = {func.__name__}')
        begin_time = time.time()
        func(*args, **kwargs)

        duration = time.time() - begin_time

        print(f"inner elapsed time: {duration}")
    return inner


def auth1(func):
    print('this is auth1')

    def inner1(*args, **kwargs):
        print(f'this is a inner1 {args}: {kwargs}, func = {func.__name__}')
        begin_time = time.time()
        func(*args, **kwargs)

        duration = time.time() - begin_time

        print(f"inner1 elapsed time: {duration}")
    return inner1


@auth1
@auth
def do_something(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    time.sleep(1)


if __name__ == '__main__':
    print(do_something.__closure__)
    do_something('test1', 'test2', 'test3')
    '''
    解析时执行， 从下到上解析
    do_something = auth(do_something) -> this is auth
    do_something = auth1(do_something) -> this is auth1
    实际调用时执行
    auth1.inner1('test1', 'test2', 'test3') -> this is a inner1
    auth.inner('test1', 'test2', 'test3') -> this is a inner
    do_something('test1', 'test2', 'test3') -> a = test1...
    inner elasped
    inner1 elasped
    
    为啥没有执行时，就能传递回来内嵌函数？？？
    
    
    '''

