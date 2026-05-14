class RomanNumber:
    """
    A class that represents a Roman numeral.
    It can be initialized with either a Roman numeral string or an integer (1 to 3999).
    Provides methods for conversion, arithmetic, and representation.
    """

    _roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    _decimal_values = [1000, 900, 500, 400, 100,
                       90, 50, 40, 10, 9, 5, 4, 1]
    _roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                      'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    def __init__(self, value):
        """
        Initialize a RomanNumber instance.

        Args:
            value (str or int): The Roman numeral as a string or an integer (1 to 3999).
        """
        if isinstance(value, str):
            if self.is_roman(value):
                self.rom_value = value
                self.int_value = self._to_decimal(value)
            else:
                print("Error")
                self.rom_value = None
                self.int_value = None
        elif isinstance(value, int):
            if self.is_int(value):
                self.int_value = value
                self.rom_value = self._to_roman(value)
            else:
                print("Error")
                self.rom_value = None
                self.int_value = None
        else:
            print("Error")
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        """
        Return the decimal value of the RomanNumber.

        Returns:
            int or None: The integer value, or None if invalid.
        """
        return self.int_value

    def roman_number(self):
        """
        Return the Roman numeral string of the RomanNumber.

        Returns:
            str or None: The Roman numeral string, or None if invalid.
        """
        return self.rom_value

    @staticmethod
    def is_roman(val):
        """
        Check if the given string is a valid Roman numeral.

        Args:
            val (str): The string to check.

        Returns:
            bool: True if valid Roman numeral, False otherwise.
        """
        if not isinstance(val, str) or len(val) == 0:
            return False

        allowed = set('IVXLCDM')
        if not all(ch in allowed for ch in val):
            return False

        for sym in ['V', 'L', 'D']:
            if sym * 2 in val:
                return False

        for sym in ['I', 'X', 'C', 'M']:
            if sym * 4 in val:
                return False

        invalid_patterns = [
            'VX', 'VL', 'VC', 'VD', 'VM',
            'IL', 'IC', 'ID', 'IM',
            'XD', 'XM',
            'LC', 'LM',
            'DM'
        ]

        for ptrn in invalid_patterns:
            if ptrn in val:
                return False

        subtractive = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        for combo in subtractive:
            if val.count(combo) > 1:
                return False

        roman_vals = RomanNumber._roman_values
        prev_val = float('inf')
        pos = 0
        length = len(val)

        while pos < length:
            if pos + 1 < length and roman_vals[val[pos]] < roman_vals[val[pos + 1]]:
                cur_val = roman_vals[val[pos + 1]] - roman_vals[val[pos]]
                if roman_vals[val[pos + 1]] > 10 * roman_vals[val[pos]]:
                    return False
                pos += 2
            else:
                cur_val = roman_vals[val[pos]]
                pos += 1

            if cur_val > prev_val:
                return False

            prev_val = cur_val

        return True

    @staticmethod
    def is_int(val):
        """
        Check if an integer can be represented as a Roman numeral (1..3999).

        Args:
            val (int): The integer value to check.

        Returns:
            bool: True if representable as a Roman numeral, False otherwise.
        """
        if not isinstance(val, int):
            return False

        if val < 1 or val > 3999:
            return False

        return True

    def _to_decimal(self, roman):
        """
        Convert a Roman numeral string to its decimal value.

        Args:
            roman (str): The Roman numeral string.

        Returns:
            int: The corresponding decimal value.
        """
        total = 0
        prev_val = 0

        for ch in reversed(roman):
            cur_val = self._roman_values[ch]

            if cur_val < prev_val:
                total -= cur_val
            else:
                total += cur_val

            prev_val = cur_val

        return total

    def _to_roman(self, decimal):
        """
        Convert an integer to its Roman numeral string representation.

        Args:
            decimal (int): The integer to be converted (1..3999).

        Returns:
            str: The Roman numeral representation.
        """
        result = ""
        num = decimal

        for idx in range(len(self._decimal_values)):
            while num >= self._decimal_values[idx]:
                result += self._roman_symbols[idx]
                num -= self._decimal_values[idx]

        return result

    def __str__(self):
        """
        Return the Roman numeral string representation of the object.

        Returns:
            str: The Roman numeral, or 'None' if invalid.
        """
        if self.rom_value is None:
            return "None"
        return self.rom_value

    def __repr__(self):
        """
        Debug representation of the RomanNumber object.

        Returns:
            str: Debug string.
        """
        if self.rom_value is None:
            return "None"
        return f"{self.rom_value}"

    def __add__(self, other):
        """
        Add two RomanNumber objects.

        Args:
            other (RomanNumber): Another RomanNumber instance.

        Returns:
            RomanNumber: The sum as a new RomanNumber, or RomanNumber(None) if operation is not possible.

        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                result = self.int_value + other.int_value
                if self.is_int(result):
                    return RomanNumber(result)
        return RomanNumber(None)

    def __sub__(self, other):
        """
        Subtract one RomanNumber from another.

        Args:
            other (RomanNumber): Another RomanNumber instance.

        Returns:
            RomanNumber: The difference as a new RomanNumber,
            or RomanNumber(None) if the result is below 1.

        """
        if isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                result = self.int_value - other.int_value
                if self.is_int(result):
                    return RomanNumber(result)
        return RomanNumber(None)


num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
