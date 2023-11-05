from dataclasses import dataclass

from .alphabet import alphabet


@dataclass
class Keyboard:
    def forward(self, letter: str) -> int:
        return alphabet.index(letter.upper())

    def backward(self, signal: int) -> str:
        return alphabet[signal]
