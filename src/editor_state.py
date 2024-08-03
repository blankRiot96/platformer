import pygame

from src import shared, utils
from src.chunk_handler.creator import ChunkCreator
from src.enums import State


class EditorState:

    def __init__(self) -> None:
        self.chunk_creator = ChunkCreator()
        self.cam_speed = 200
        self.scaling_factor = 1.0
        self.scaled_cam = shared.camera.offset.copy()
        self.scaled_mp = pygame.Vector2()

        self.font = utils.load_font(None, 32)

    def update(self):
        shared.mouse_pos /= self.scaling_factor
        if shared.keys[pygame.K_a]:
            self.scaled_cam.x -= self.cam_speed * shared.dt
        if shared.keys[pygame.K_w]:
            self.scaled_cam.y -= self.cam_speed * shared.dt
        if shared.keys[pygame.K_s]:
            self.scaled_cam.y += self.cam_speed * shared.dt
        if shared.keys[pygame.K_d]:
            self.scaled_cam.x += self.cam_speed * shared.dt

        shared.camera.offset = self.scaled_cam / self.scaling_factor

        self.chunk_creator.update()

        if shared.kp[pygame.K_ESCAPE]:
            shared.camera.offset = shared.player.pos.copy() - (
                pygame.Vector2(shared.srect.size) / 2
            )
            self.chunk_creator.dump_files()
            shared.next_state = State.GAME

    def draw(self):
        self.chunk_creator.render()
        scaled_screen = pygame.transform.scale_by(shared.screen, self.scaling_factor)
        shared.screen.fill("black")

        pygame.draw.rect(
            shared.screen, "red", scaled_screen.get_rect().inflate(10, 10), width=5
        )
        shared.screen.blit(scaled_screen, (0, 0))
        shared.screen.blit(
            self.font.render(
                f"No. of chunks LOADED: {len(self.chunk_creator.on_screen_chunks)}",
                True,
                (200, 200, 200),
                "brown",
            ),
            (10, 20),
        )
