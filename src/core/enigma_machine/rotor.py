from dataclasses import dataclass

from .alphabet import alphabet


@dataclass
class Rotor:
    left: str
    right: str
    notch: str

    def __init__(self, wiring: str, notch: str) -> None:
        self.left = alphabet
        self.right = wiring
        self.notch = notch

    def forward(self, signal: int) -> int:
        letter = self.right[signal]
        return self.left.index(letter)

    def backward(self, signal: int) -> int:
        letter = self.left[signal]
        return self.right.index(letter)

    def rotate(self, steps: int = 1) -> None:
        for _ in range(steps):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to_letter(self, letter: str) -> None:
        steps = self.right.index(letter)
        self.rotate(steps)
