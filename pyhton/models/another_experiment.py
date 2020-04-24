from multimethod import multimethod
from doctest import testmod

class ClassWithStaticAndOverload:
    worker_name = "Vasia"

    @staticmethod
    def do_work():
        pass

    def sing_a_song(self):
        print(ClassWithStaticAndOverload.worker_name)

    @multimethod
    def print_data(self, first, second):
        print(str(first) + "Hop sa" + str(second))

    @multimethod
    def print_data(self, first, second):
        """
        returns sum of two integers
        >>>obj = ClassWithStaticAndOverload()
        >>> obj.print_data(10, 20)
        30
        """
        print(str(first + second))
        return first + second


def create_tuple(first, second):
    """
    >>> create_tuple(10, 20)
    (10, 20)
    """
    return (first, second)


if __name__ == "__main__":
    my_object = ClassWithStaticAndOverload()
    my_object.print_data(23, 45)
    my_object.print_data("34", "78")
