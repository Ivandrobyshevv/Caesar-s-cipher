class Caesar:
    def __init__(self, alfabet: str) -> None:
        self.alfabet = alfabet

    def encryption_caesar(self, text: str, shift: int) -> str:
        encryption_text = []
        for char in text:
            if check_symbol(char) and check_lower_case(char):
                encryption_char = self.get_encryption_char(char.upper(), shift)
                encryption_text.append(encryption_char.lower())
            elif check_symbol(char):
                encryption_char = self.get_encryption_char(char, shift)
                encryption_text.append(encryption_char)
            else:
                encryption_text.append(char)

        return ''.join(encryption_text)

    # def encryption_caesar(self, text: str, shift: int) -> str:
    #     pass

    def get_encryption_char(self, char: str, shift: int):
        index = self.get_index(char)
        tmp = ((index + shift) % len(self.alfabet)) - 1
        return self.alfabet[tmp]

    def get_index(self, char: str) -> int:
        return self.alfabet.index(char) + 1


def check_symbol(char: str) -> bool:
    return char.isalpha()


def check_lower_case(char: str) -> bool:
    return char.islower()
