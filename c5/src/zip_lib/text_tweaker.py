from pathlib import Path
import re
from zip_processor import ZipProcessor


class TextTweaker(ZipProcessor):
    def __init__(self, archive: Path) -> None:
        super().__init__(archive)
        self.find: str
        self.replace: str

    def find_and_replace(self, find: str, replace: str) -> "TextTweaker":
        self.find = find
        self.replace = replace
        return self

    def transform(self, extracted: Path) -> None:
        input_text = extracted.read_text()
        output_text = re.sub(self.find, self.replace, input_text)
        extracted.write_text(output_text)

if __name__ == "__main__":
    sample_zip = Path(
        "/home/mario/DEV/python/python_object_oriented_programing/c5/src/sample.zip")
    zr = TextTweaker(sample_zip)
    zr.find_and_replace("xyzzy", "plover's egg")
    zr.process_files("*.md")
