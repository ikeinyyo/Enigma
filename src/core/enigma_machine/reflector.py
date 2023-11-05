from dataclasses import dataclass

from .alphabet import alphabet


@dataclass
class Reflector:
    left: str
    right: str

    def __init__(self, wiring: str) -> None:
        self.left = alphabet
        self.right = wiring

    def reflect(self, signal: int) -> int:
        letter = self.right[signal]
        return self.left.index(letter)
