from core.enigma_machine import Enigma, Keyboard, Plugboard, Reflector, Rotor, alphabet


def main() -> None:
    """
    Enigma Configuration:

    Reflectors: A
    Rotors: I - II - III
    Plugboard: A-R, G-K, O-X
    """
    keyboard = Keyboard()
    plugboard = Plugboard(["AR", "GK", "OX"])
    I = Rotor(alphabet.wiring_enigma_rotor_I, alphabet.notch_enigma_rotor_I)
    II = Rotor(alphabet.wiring_enigma_rotor_II, alphabet.notch_enigma_rotor_II)
    III = Rotor(alphabet.wiring_enigma_rotor_III, alphabet.notch_enigma_rotor_III)
    A = Reflector(alphabet.wiring_enigma_reflector_A)
    enigma = Enigma(keyboard, plugboard, A, [I, II, III])

    word = "LVHX KPSTV"
    print(enigma.encipher(word))


if __name__ == "__main__":
    main()
