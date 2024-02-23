from model.media_loader_abstract import MediaLoaderAbstract
from typing import List


class Wav(MediaLoaderAbstract):
    pass


class Ogg(MediaLoaderAbstract):
    ext = '.ogg'

    def play(self) -> None:
        pass


class GenericClass():
    def __init__(self, int_list: List[int]) -> None:
        print(int_list)
        self.x = int_list


if __name__ == '__main__':
    # type error: Can't instantiate abstract class Wav with abstract methods ext, play
    # x = Wav()
    
    x = Ogg()
    print(x)
    x.method_whit_body()

    y = GenericClass('String')
    print(y)

    z = GenericClass([2, 3, 4])
    print(z)
    
    tuple1 = (1, 2, 3)
    print(tuple1)
    
    dict1 = {'x': 1, 'y': 2}
    print(dict1)
    dict1['x'] = 3
    print(dict1)
    