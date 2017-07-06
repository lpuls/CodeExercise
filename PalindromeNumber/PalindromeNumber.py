class PalindromeNumber(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n = 0
        temp = x
        while temp:
            n = n * 10 + temp % 10
            temp = temp / 10
        return n == x
