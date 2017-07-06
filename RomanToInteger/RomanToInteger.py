class RomanToInteger(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        pow = 0
        number = 0
        s = s.upper()
        length = len(s)
        for i in range(0, length):
            item = s[length - i - 1]
            if pow > roman_dict[item]:
                number -= roman_dict[item]
            else:
                number += roman_dict[item]
                pow = roman_dict[item]
        return number
