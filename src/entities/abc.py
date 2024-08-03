import abc

import pygame

from src import shared
from src.chunk_handler.types import Cell
from src.shared import CHUNK_SIZE, CHUNK_TILES, TILE_SIDE, TILE_SIZE


class BaseEntity(abc.ABC):
    """Base class for all future entities"""

    def __init__(self, cell: Cell, chunk_pos: Cell) -> None:
        self.cell = cell
        self.chunk_pos = chunk_pos
        self.pos = pygame.Vector2(self.cell) * TILE_SIDE
        ## Setting it to its chunk
        self.pos += pygame.Vector2(self.chunk_pos) * CHUNK_SIZE
        self.surf = pygame.Surface(TILE_SIZE)
        self.rect = pygame.Rect(self.pos, TILE_SIZE)

    def on_removal(self):
        pass

    def update(self) -> None:
        mx, my = self.pos // TILE_SIDE
        self.mx, self.my = mx, my
        chunk_pos = (mx // CHUNK_TILES, my // CHUNK_TILES)
        entity_cell = (mx, my) - (pygame.Vector2(chunk_pos) * CHUNK_TILES)

        self.chunk_pos = (int(chunk_pos[0]), int(chunk_pos[1]))
        self.cell = (int(entity_cell[0]), int(entity_cell[1]))

    def render(self) -> None:
        shared.screen.blit(self.surf, shared.camera.transform(self.rect))
