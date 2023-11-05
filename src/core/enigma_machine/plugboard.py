from dataclasses import dataclass
from typing import List

from .alphabet import alphabet


@dataclass
class Plugboard:
    left: str = alphabet
    right: str = alphabet

    def __init__(self, pairs: List[str]) -> None:
        self._configure_pairs(pairs)

    def _configure_pairs(self, pairs: List[str]) -> None:
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            index_A = self.left.index(A)
            index_B = self.left.index(B)
            self.left = self.left[:index_A] + B + self.left[index_A + 1 :]
            self.left = self.left[:index_B] + A + self.left[index_B + 1 :]

    def forward(self, signal: int) -> int:
        letter = self.right[signal]
        return self.left.index(letter)

    def backward(self, signal: int) -> int:
        letter = self.left[signal]
        return self.right.index(letter)
