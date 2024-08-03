import pygame

from src import shared

from .abc import BaseEntity


class Tile(BaseEntity):
    def __init__(self, cell: tuple[int, int], chunk_pos: tuple[int, int]) -> None:
        super().__init__(cell, chunk_pos)
        self.surf = pygame.Surface(self.rect.size)
        self.surf.fill("brown")
        shared.tiles.append(self)

    def on_removal(self):
        super().on_removal()
        shared.tiles.remove(self)
