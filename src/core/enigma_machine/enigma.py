from dataclasses import dataclass
from typing import List

from .keyboard import Keyboard
from .plugboard import Plugboard
from .reflector import Reflector
from .rotor import Rotor


@dataclass
class Enigma:
    keyboard: Keyboard
    plugboard: Plugboard
    reflector: Reflector
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

    def encipher(self, message: str) -> str:
        encrypted_message = ""
        for letter in message.upper():
            encrypted_message += self.encipher_letter(letter)
        return encrypted_message

    def encipher_letter(self, letter: str) -> str:
        try:
            signal = self.keyboard.forward(letter)
            signal = self.plugboard.forward(signal)

            for rotor in self.rotors[::-1]:
                signal = rotor.forward(signal)

            signal = self.reflector.reflect(signal)

            for rotor in self.rotors:
                signal = rotor.backward(signal)

            signal = self.plugboard.backward(signal)
            return self.keyboard.backward(signal)
        except:
            return letter
