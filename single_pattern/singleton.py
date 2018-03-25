# coding = utf-8


class Singleton(object):
    """
    单例类
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class LazySingleton(object):
    """
    单例懒汉式实例化
    """
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print('__init__ method called..')
        else:
            print('Instance already created:', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return  cls.__instance


if __name__ == '__main__':
    # Singleton
    s = Singleton()
    print('Object created', s)

    s1 = Singleton()
    print('Object created', s1)

    # LazySingleton
    ls = LazySingleton()
    print('Object created', LazySingleton.get_instance())
    s2 = LazySingleton()
    print(s2)
