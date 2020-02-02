
def dict_practice():
    d = {'mike': 10, 'lucy': 2, 'ben': 30}
    d = sorted(d.items(), key = lambda x: x[1], reverse = True)
    print(d)




if __name__ == '__main__':
    dict_practice()

