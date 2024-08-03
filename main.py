import pygame

from src import shared
from src.camera import Camera
from src.state_manager import StateManager

pygame.init()
shared.screen = pygame.display.set_mode((1100, 650))
shared.clock = pygame.Clock()
shared.srect = shared.screen.get_rect()
shared.camera = Camera()
state_manager = StateManager()

while True:
    shared.events = pygame.event.get()
    shared.dt = shared.clock.tick(60) / 1000
    shared.dt = max(shared.dt, 0.1)
    shared.keys = pygame.key.get_pressed()
    shared.kp = pygame.key.get_just_pressed()
    shared.kr = pygame.key.get_just_released()
    shared.mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    shared.mouse_press = pygame.mouse.get_pressed()
    for event in shared.events:
        if event.type == pygame.QUIT:
            raise SystemExit

    state_manager.update()

    shared.screen.fill("black")
    state_manager.draw()
    pygame.display.flip()
