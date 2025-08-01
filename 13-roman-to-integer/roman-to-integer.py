class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_integer = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman_to_integer[s[i]] < roman_to_integer[s[i+1]]:
                result -= roman_to_integer[s[i]]
            else:
                result += roman_to_integer[s[i]] 
        return result  