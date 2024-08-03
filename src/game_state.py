import pygame

from src import shared
from src.camera import Camera
from src.chunk_handler.creator import ChunkCreator
from src.enums import State


class GameState:
    def __init__(self) -> None:
        shared.tiles = []
        self.chunk_creator = ChunkCreator()

    def update(self):
        self.chunk_creator._calc_center_chunk()

        if shared.kp[pygame.K_ESCAPE]:
            self.chunk_creator.dump_files()
            shared.next_state = State.EDITOR

        for chunk in self.chunk_creator.on_screen_chunks.values():
            for entity in chunk.cells.values():
                entity.update()

    def draw(self):
        self.chunk_creator.render_chunks(draw_border=False)
