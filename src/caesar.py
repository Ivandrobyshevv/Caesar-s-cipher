class Caesar:
    def __init__(self, alfabet: str) -> None:
        self.alfabet = alfabet

    def encryption_caesar(self, text: str, shift: int) -> str:
        encryption_text = []
        for char in text:
            if check_symbol(char) and check_lower_case(char):
                encryption_char = self.__get_encryption_char(char.upper(), shift)
                encryption_text.append(encryption_char.lower())
            elif check_symbol(char):
                encryption_char = self.__get_encryption_char(char, shift)
                encryption_text.append(encryption_char)
            else:
                encryption_text.append(char)

        return ''.join(encryption_text)

    def decryption_caesar(self, text: str, shift: int) -> str:
        decryption_text = []
        for char in text:
            if check_symbol(char) and check_lower_case(char):
                decryption_char = self.__get_decryption_char(char.upper(), shift)
                decryption_text.append(decryption_char.lower())

            elif check_symbol(char):
                decryption_char = self.__get_decryption_char(char, shift)
                decryption_text.append(decryption_char)

            else:
                decryption_text.append(char)

        return ''.join(decryption_text)

    def __get_encryption_char(self, char: str, shift: int) -> str:
        index = self.__get_index(char)
        tmp = ((index + shift) % len(self.alfabet)) - 1
        return self.alfabet[tmp]

    def __get_decryption_char(self, char: str, shift: int) -> str:
        index = self.__get_index(char)
        tmp = ((index - shift) % len(self.alfabet)) - 1
        return self.alfabet[tmp]

    def __get_index(self, char: str) -> int:
        return self.alfabet.index(char) + 1


def check_symbol(char: str) -> bool:
    return char.isalpha()


def check_lower_case(char: str) -> bool:
    return char.islower()
