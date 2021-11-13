class man:
    __slots__ = ()
    pass


class Taro(man):
    __slots__ = ('name','age')

    def __init__(self):
        self.name = 'taro'
        self.age = '15'



taro = Taro()
#taro.height = 170
#taro.weight = 58



print(taro.__dict__)
