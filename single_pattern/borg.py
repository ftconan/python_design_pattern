# coding = utf-8


class Borg(object):
    """
    Monostate单例模式
    """
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


class NewBorg(object):
    """
    使用__new__实现
    """
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(NewBorg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b.x = 4

    # b and b1 are distinct objects
    print("Borg Object 'b':", b)
    print("Borg Object 'b1':", b1)
    # b and b1 share same status
    print("Object State 'b':", b.__dict__)
    print("Object State 'b1':", b1.__dict__)

    # NewBorg
    print(NewBorg())
