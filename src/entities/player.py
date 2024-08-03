import pygame

from src import shared, utils
from src.chunk_handler.types import Cell

from .abc import BaseEntity


class Player(BaseEntity):
    def __init__(self, cell: tuple[int, int], chunk_pos: tuple[int, int]) -> None:
        super().__init__(cell, chunk_pos)
        self.surf = pygame.Surface(self.rect.size)
        self.surf.fill("white")
        shared.player = self
        self.velocity = 100.0
        self.vertical_velocity = 0.0
        self.gravity = 10.0
        self.max_vertical_velocity = 100.0

    def update(self):
        super().update()
        if self.vertical_velocity < self.max_vertical_velocity:
            self.vertical_velocity += self.gravity * shared.dt
        else:
            self.vertical_velocity = self.max_vertical_velocity

        dx = 0
        if shared.keys[pygame.K_a]:
            dx = -1
        if shared.keys[pygame.K_d]:
            dx = 1
        dx *= self.velocity * shared.dt
        if shared.kp[pygame.K_SPACE]:
            self.vertical_velocity = -100.0

        dy = self.vertical_velocity * shared.dt
        for tile in shared.tiles:
            if self.rect.move(dx, 0).inflate(0, -1).colliderect(tile.rect):
                dx = 0
            if self.rect.move(0, dy).inflate(-2, 0).colliderect(tile.rect):
                self.vertical_velocity = 0.0
                dy = 0

        self.pos.x += dx
        self.pos.y += dy
        self.rect.topleft = self.pos
        shared.camera.attach_to(self.pos)

    def render(self):
        super().render()
