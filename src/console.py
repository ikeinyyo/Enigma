import argparse
import json
from typing import Dict

from core.enigma_machine import Enigma, Keyboard, Plugboard, Reflector, Rotor, alphabet

CLOSE_MESSAGE = "EXIT"


def main(config_filepath: str) -> None:
    enigma = initialize_enigma(config_filepath)
    print(enigma)

    message = ""

    while message.upper() != CLOSE_MESSAGE:
        enigma = initialize_enigma(config_filepath)
        message = input(f"Message (enter '{CLOSE_MESSAGE}' to close app): ")
        enciphered = enigma.encipher(message)
        print(f"Enciphered: {enciphered}\n")


def get_config(config_filepath: str) -> Dict:
    try:
        with open(config_filepath, "r") as in_file:
            config = json.load(in_file)
        plugboard_pairs = config["plugboard"]
        key = config["key"]
        rings = config["rings"]
        num_rotors = config["num_rotors"]
    except:
        print("Error loading Enigma configuration")
        plugboard_pairs = ["AR", "GK", "OX"]
        key = "SYE"
        rings = [14, 2, 8]
        num_rotors = 3

    return {
        "plugboard_pairs": plugboard_pairs,
        "key": key,
        "rings": rings,
        "num_rotors": num_rotors,
    }


def initialize_enigma(config_filepath: str) -> Enigma:
    config = get_config(config_filepath)
    keyboard = Keyboard()
    plugboard = Plugboard(config["plugboard_pairs"])
    I = Rotor(alphabet.wiring_enigma_rotor_I, alphabet.notch_enigma_rotor_I)
    II = Rotor(alphabet.wiring_enigma_rotor_II, alphabet.notch_enigma_rotor_II, True)
    III = Rotor(alphabet.wiring_enigma_rotor_III, alphabet.notch_enigma_rotor_III)
    IV = Rotor(alphabet.wiring_enigma_rotor_IV, alphabet.notch_enigma_rotor_IV)
    V = Rotor(alphabet.wiring_enigma_rotor_V, alphabet.notch_enigma_rotor_V)
    A = Reflector(alphabet.wiring_enigma_reflector_A)
    B = Reflector(alphabet.wiring_enigma_reflector_B)
    enigma = Enigma(keyboard, plugboard, B, [I, II, III, IV, V][: config["num_rotors"]])
    enigma.set_key(config["key"])
    enigma.set_rings(config["rings"])
    return enigma


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--config_filepath", required=False, help="Enigma configuration file"
    )
    args = parser.parse_args()
    main(args.config_filepath)
