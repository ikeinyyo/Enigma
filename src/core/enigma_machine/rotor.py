from dataclasses import dataclass

from .alphabet import alphabet


@dataclass
class Rotor:
    left: str
    right: str
    notch: str
    rotate_in_notch: bool

    def __init__(self, wiring: str, notch: str, rotate_in_notch: bool = False) -> None:
        self.left = alphabet
        self.right = wiring
        self.notch = notch
        self.rotate_in_notch = rotate_in_notch

    def forward(self, signal: int) -> int:
        letter = self.right[signal]
        return self.left.index(letter)

    def backward(self, signal: int) -> int:
        letter = self.left[signal]
        return self.right.index(letter)

    def rotate(self, steps: int = 1, forward=True) -> None:
        for _ in range(steps):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[-1] + self.left[:-1]
                self.right = self.right[-1] + self.right[:-1]

    def rotate_to_letter(self, letter: str) -> None:
        steps = self.left.index(letter)
        self.rotate(steps)

    def set_ring(self, ring: int) -> None:
        self.rotate(ring - 1, False)

        notch_index = alphabet.index(self.notch)
        self.notch = alphabet[(notch_index - ring + 1) % len(alphabet)]

    def is_in_notch(self) -> bool:
        return self.left[0] == self.notch

    def __str__(self) -> str:
        return f"N: {self.notch} - F: {self.left[0]}"
