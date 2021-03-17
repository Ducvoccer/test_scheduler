class Test():
    __a = 0
    _b=1
    def __init__(self):
        self.__a = 5
        # print(self.__a)
    def __get_a(self):
        print('comehere')
        return __a
test = Test()
# test.__get_a()
print(test._b)
print(test.__a)
# print(test.__a)
