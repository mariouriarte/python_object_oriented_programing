from pathlib import Path
from typing import Protocol


class Playable(Protocol):
    pass


class AudioFile:
    ext: str

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath

    def play(self):
        pass


class MP3File(AudioFile):
    ext = ".mp3"

    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")


class WavFile(AudioFile):
    ext = ".wav"

    def play(self) -> None:
        print(f"playing {self.filepath} as wav")


class OggFile(AudioFile):
    ext = ".ogg"

    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")


class FlacFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath

    def play(self) -> None:
        print(f"playing {self.filepath} as flac")


class MediaPlayer:

    def __init__(self, audio_file: AudioFile):
        self.audio_file = audio_file

    def play_song(self):
        self.audio_file.play()

    def change_song(self, audio_file: AudioFile):
        self.audio_file = audio_file


if __name__ == '__main__':
    ogg = OggFile(Path("c3/src/polymorphism/audio.ogg"))
    # ogg.play()
    # raise error
    # wav = WavFile(Path("c3/src/polymorphism/audio.ogg"))

    media_player = MediaPlayer(ogg)
    media_player.play_song()

    mp3 = MP3File(Path("c3/src/polymorphism/audio.mp3"))
    media_player.change_song(mp3)
    media_player.play_song()

    # Duck typing
    flac = FlacFile(Path("c3/src/polymorphism/audio.flac"))
    media_player.change_song(flac)
    media_player.play_song()
