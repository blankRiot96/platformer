import typing as t

import pygame

from src import shared
from src.editor_state import EditorState
from src.enums import State
from src.game_state import GameState


class StateLike(t.Protocol):
    def update(self): ...

    def draw(self): ...


class StateManager:
    def __init__(self) -> None:
        shared.next_state = None
        self.state_map: dict[State, StateLike] = {
            State.GAME: GameState,
            State.EDITOR: EditorState,
        }
        self.current_state = self.state_map.get(State.GAME)()

    def update(self):
        self.current_state.update()
        if shared.next_state is not None:
            self.current_state = self.state_map.get(shared.next_state)()
            shared.next_state = None

    def draw(self):
        self.current_state.draw()
