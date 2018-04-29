# coding = utf-8

# author: conan
# date: 2018/4/29


class Animal(object):
    """
    animal
    """
    def do_say(self):
        pass


class Dog(Animal):
    """
    dog
    """
    def do_say(self):
        print('Bhow Bhow!!')


class  Cat(Animal):
    """
    cat
    """
    def do_say(self):
        print('Meow Meow!!')


class ForestFactory(object):
    """
    forest factory defined
    """
    def make_sound(self, object_type):
        """
        sound
        :param object_type:
        :return:
        """
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('Which animal should make_sound Dog or Cat?')
    ff.make_sound(animal)
