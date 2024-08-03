from __future__ import annotations

import typing as t

import pygame

if t.TYPE_CHECKING:
    from src.camera import Camera
    from src.entities import Player, Tile
    from src.enums import State

# Constants
TILE_SIDE = 32
TILE_SIZE = (TILE_SIDE, TILE_SIDE)
CHUNK_TILES = 6
CHUNK_SIZE = CHUNK_TILES * TILE_SIDE

# Canvas
screen: pygame.Surface
srect: pygame.Rect
camera: Camera

# Events
events: list[pygame.event.Event]
mouse_pos: pygame.Vector2
mouse_press: tuple[int, ...]
keys: list[bool]
kp: list[bool]
kr: list[bool]
dt: float
clock: pygame.Clock

# Entities
player: Player
tiles: list[Tile]

# ?
next_state: State | None
