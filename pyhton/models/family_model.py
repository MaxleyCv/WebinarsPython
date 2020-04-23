from abc import ABC, abstractmethod


class Mother:
    def __init__(self, age=0):
        self.age = age
        print("Mother in da haus")

    def do_work(self):
        print("I'm working")

    def do_house_work(self):
        print("WORK WORK WORK")


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Father(AbstractParent):
    def __init__(self):
        print("Father in da haus")

    def play_guitar(self):
        print("BRIN BRIN BRIN")

    def do_house_work(self):
        print("MUSICCA & beer")


class Daughter(Mother, Father):
    def __init__(self, age=0):
        Mother.__init__(self, age)
        Father.__init__(self)

    def do_work(self):
        print("I'm da horse")

    def hello_friend(self):
        print("Hai, M dater")


class Friend:
    pass

def greet_father(father: Father):
    print("time for beer!")
    father.play_guitar()


def greet_mother(mother: Mother):
    print("HAAAAAAAAI")
    mother.do_work()


if __name__ == "__main__":
    daughter = Daughter()
    greet_mother(daughter)
    daughter.hello_friend()
    greet_father(daughter)
    daughter.do_house_work()

    #list
    povtorka_list = ["programming2", "mathan"]

    #tuple
    vasian = ("0.5", daughter)

    #set
    my_set = {23, 11, "vasian"}

    #frozenset
    anotherset = frozenset([1, 2, 3])

    #dictionary
    my_dict = {1:"first", "2":123}

