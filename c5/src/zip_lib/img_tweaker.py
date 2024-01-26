from PIL import Image
from pathlib import Path
from zip_processor_copy_file import ZipProcessorCopyFile


class ImgTweaker(ZipProcessorCopyFile):
    def transform(self, extracted: Path) -> None:
        image = Image.open(extracted)
        scaled = image.resize(size=(640, 960))
        scaled.save(extracted)


if __name__ == "__main__":
    sample_zip = Path(
        "/home/mario/DEV/python/python_object_oriented_programing/c5/src/sample.zip")
    zr = ImgTweaker(sample_zip)
    zr.process_files("*.png")
