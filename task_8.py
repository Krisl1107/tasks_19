MORSE_CODE = {

    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.',
    'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..',
    'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...',
    'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
    'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
    'Ю': '..--', 'Я': '.-.-'
}


REV_MORSE_EN = {val: key for key, val in MORSE_CODE.items() if 'A' <= key <= 'Z'}
REV_MORSE_RU = {val: key for key, val in MORSE_CODE.items() if 'А' <= key <= 'Я'}


VOWELS_EN = ['A', 'E', 'I', 'O', 'U']
VOWELS_RU = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']


CONS_EN = [ch for ch in MORSE_CODE.keys() if ch.isalpha() and ch not in VOWELS_EN]
CONS_RU = [ch for ch in MORSE_CODE.keys() if ch.isalpha() and ch not in VOWELS_RU]


class MorseMsg:
    """
    A class to handle Morse code messages and decoding into Latin and Cyrillic alphabets.

    Attributes:
        message (str): The Morse code message consisting of "." and "-" separated by spaces.
    """

    def __init__(self, message):
        """
        Initializes a MorseMsg instance with a Morse code message.

        Args:
            message (str): Encoded Morse message, e.g., "... --- ..."
        """
        self.message = message

    def __str__(self):
        """
        Returns the original Morse code message (encrypted form).

        Returns:
            str: The Morse code message.
        """
        return self.message

    def eng_decode(self):
        """
        Decodes the Morse code message into Latin alphabet letters.

        Returns:
            str: The decoded message in Latin letters.
        """
        chars = []

        for code in self.message.split():
            letter = REV_MORSE_EN.get(code, '')
            if letter and 'A' <= letter <= 'Z':
                chars.append(letter)
        return ''.join(chars)

    def ru_decode(self):
        """
        Decodes the Morse code message into Cyrillic alphabet letters.

        Returns:
            str: The decoded message in Cyrillic letters.
        """
        chars = []

        for code in self.message.split():
            letter = REV_MORSE_RU.get(code, '')
            if letter and 'А' <= letter <= 'Я':
                chars.append(letter)
        return ''.join(chars)

    def get_vowels(self, lang):
        """
        Gets the list of vowels in the message, in order.

        Args:
            lang (str): The language code ('eng' or 'ru').

        Returns:
            list: List of vowels present in the message in the order they appear.
        """
        if lang == 'eng':
            vowels = VOWELS_EN
        elif lang == 'ru':
            vowels = VOWELS_RU
        else:
            raise ValueError("Language must be 'eng' or 'ru'.")


        if lang == 'eng':
            decoded_message = self.eng_decode()
        elif lang == 'ru':
            decoded_message = self.ru_decode()
        else:
            raise ValueError("Language must be 'eng' or 'ru'.")

        result = [ch for ch in decoded_message if ch in vowels]
        return result

    def get_consonants(self, lang):
        """
        Gets the list of consonants in the message, in order.

        Args:
            lang (str): The language code ('eng' or 'ru').

        Returns:
            list: List of consonants present in the message in the order they appear.
        """
        if lang == 'eng':
            consonants = CONS_EN
        elif lang == 'ru':
            consonants = CONS_RU
        else:
            raise ValueError("Language must be 'eng' or 'ru'.")

        if lang == 'eng':
            decoded_message = self.eng_decode()
        elif lang == 'ru':
            decoded_message = self.ru_decode()
        else:
            raise ValueError("Language must be 'eng' or 'ru'.")


        result = [ch for ch in decoded_message if ch in consonants]
        return result

msgs = []
msgs.append(MorseMsg('.. .-.. .. -.- . .--. -.-- - .... --- -.'))
msgs.append(MorseMsg('-- --- .-.- .--. .-. --- --. .-. .- -- -- .-'))
for msg in msgs:
    print(msg)
print(msgs[0].eng_decode())
print(msgs[0].get_vowels('eng'))
print(msgs[0].get_consonants('eng'))
print(msgs[1].ru_decode())
print(msgs[1].get_vowels('ru'))
print(msgs[1].get_consonants('ru'))
