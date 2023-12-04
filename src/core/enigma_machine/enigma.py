from dataclasses import dataclass
from typing import List

from .alphabet import alphabet
from .keyboard import Keyboard
from .plugboard import Plugboard
from .reflector import Reflector
from .rotor import Rotor


@dataclass
class Enigma:
    keyboard: Keyboard
    plugboard: Plugboard
    reflector: Reflector
    key: str
    rings: List[int]
    rotors: List[Rotor]

    def __init__(
        self,
        keyboard: Keyboard,
        plugboard: Plugboard,
        reflector: Reflector,
        rotors: List[Rotor],
    ) -> None:
        self.keyboard = keyboard
        self.plugboard = plugboard
        self.reflector = reflector
        self.rotors = rotors

    def _rotate_rotors(self) -> None:
        for index in range(len(self.rotors)):
            if all([rotor.is_in_notch() for rotor in self.rotors[index + 1 :]]) or any(
                [rotor.is_in_notch() and rotor.rotate_in_notch for rotor in self.rotors]
            ):
                self.rotors[index].rotate()

    def set_rings(self, rings: List[int]) -> None:
        if len(rings) != len(self.rotors):
            raise ValueError("Rings len have to be equal of number of rotors")
        self.rings = rings
        for index in range(len(self.rotors)):
            self.rotors[index].set_ring(self.rings[index])

    def set_key(self, key: str) -> None:
        if len(key) != len(self.rotors):
            raise ValueError("Key len have to be equal of number of rotors")
        self.key = key
        for index in range(len(self.rotors)):
            self.rotors[index].rotate_to_letter(self.key[index].upper())

    def encipher(self, message: str) -> str:
        encrypted_message = ""
        for letter in message.upper():
            encrypted_message += self.encipher_letter(letter)
        return encrypted_message

    def encipher_letter(self, letter: str) -> str:
        if letter not in alphabet:
            return letter

        self._rotate_rotors()

        signal = self.keyboard.forward(letter)
        signal = self.plugboard.forward(signal)

        for rotor in self.rotors[::-1]:
            signal = rotor.forward(signal)

        signal = self.reflector.reflect(signal)

        for rotor in self.rotors:
            signal = rotor.backward(signal)

        signal = self.plugboard.backward(signal)
        return self.keyboard.backward(signal)

    def __str__(self) -> str:
        rotors = "\n".join(
            [
                f"- Rotor {index} - {self.rotors[index]}"
                for index in range(len(self.rotors))
            ]
        )
        return (
            f"ENGIMA - K: {self.key} - R: {self.rings} - Plugboard: {self.plugboard}\n"
            f"{rotors}\n"
        )
