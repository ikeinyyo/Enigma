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
    II = Rotor(alphabet.wiring_enigma_rotor_II, alphabet.notch_enigma_rotor_II, True)
    III = Rotor(alphabet.wiring_enigma_rotor_III, alphabet.notch_enigma_rotor_III)
    A = Reflector(alphabet.wiring_enigma_reflector_A)
    B = Reflector(alphabet.wiring_enigma_reflector_B)
    enigma = Enigma(keyboard, plugboard, B, [I, II, III])
    enigma.set_key("DOG")
    enigma.set_rings([5, 26, 3])

    message = "HELLO WORLD THIS IS AN EXAMPLE OF HOW USE ENIGMA TO ENCIPHER A ULTRA SECRET MESSAGE"
    excepted = "GJTBB BSAUW ITGL LF NV TWLBVXM ZS KGX XMM MCYIHI QS ZFTGBWUA I KUQPB NOJLLX UCORPMC"
    enciphered = enigma.encipher(message)

    print(f"- Message:\t {message}")
    print(f"- Expected:\t {excepted}")
    print(f"- Enciphered:\t {enciphered}")
    print(f"\nIs it correct?: {enciphered == excepted}")


if __name__ == "__main__":
    main()
