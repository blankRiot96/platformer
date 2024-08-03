import typing as t


class Entity(t.Protocol):
    def update(self): ...
    def draw(self): ...


Cell: t.TypeAlias = tuple[int, int]
