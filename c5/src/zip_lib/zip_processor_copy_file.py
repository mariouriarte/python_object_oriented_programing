from __future__ import annotations
from pathlib import Path
from shutil import copy
from zip_processor import ZipProcessor


class ZipProcessorCopyFile(ZipProcessor):

    def make_backup(self) -> tuple[Path, Path]:
        res_file = self.archive_path.stem + ".res" + self.archive_path.suffix
        output = copy(self.archive_path, 'c5/src/'+res_file)
        return self.archive_path, output
