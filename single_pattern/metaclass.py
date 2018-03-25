# coding = utf-8


class MyInt(type):
    """
    自定义int类
    """
    def __call__(cls, *args, **kwargs):
        print("***** Here's My int *****", args)
        print("Now do whatever you want to do with these object ...")
        return type.__call__(cls, *args, **kwargs)


class Int(metaclass=MyInt):
    """
    int类
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MetaSingleton(type):
    """
    元类实现的单例类
    """
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == '__main__':
    i = Int(4, 5)

    # logger
    logger1 = Logger()
    logger2 = Logger()
    print(logger1, logger2)
