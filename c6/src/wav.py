from model.media_loader_abstract import MediaLoaderAbstract


class Wav(MediaLoaderAbstract):
    pass

class Ogg(MediaLoaderAbstract):
    ext = '.ogg'
    def play(self):
        pass


if __name__ == '__main__':
    # x = Wav()
    x = Ogg()
    print(x)
    x.asd()
