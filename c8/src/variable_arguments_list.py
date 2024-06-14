from __future__ import annotations
from urllib.parse import urlparse
from pathlib import Path
from typing import Dict, Any
from pprint import pprint


def get_pages(*links: str) -> None:
    for link in links:
        url = urlparse(link)
        name = "index.html" if url.path in ("", "/") else url.path
        target = Path(url.netloc.replace(".", "_")) / name
        print(f"Create {target} from {link!r}")


get_pages()
get_pages('https://www.archlinux.org')
get_pages('https://www.archlinux.org',
          'https://dusty.phillips.codes', 'https://itmaybeahack.com')


class Options(Dict[str, Any]):
    default_options: dict[str, Any] = {
        "port": 21,
        "host": "localhost",
        "username": None,
        "password": None,
        "debug": False,
    }

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(self.default_options)
        self.update(kwargs)

options = Options(username="dusty", password="Hunter2", debug=True)
pprint(options)
print(options['debug'])
