from typing import Iterator

def camelcase(s: str) -> str:
    parts: Iterator[str] = iter(s.split('_'))

    return next(parts) + ''.join((i.title() for i in parts))
