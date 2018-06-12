# encoding: utf-8
# Author: LW

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        roman_dict_2 = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        result = 0
        for x in roman_dict_2:
            if s.find(x)>=0:
                result += roman_dict_2.get(x)
                s = s.replace(x,'')

        for x in roman_dict:
            print(x,s.find(x))
            if s.find(x)>=0:
                result += roman_dict.get(x)*s.count(x)
                s = s.replace(x,'')

        return result


a = 'MCMXCIV'
# a = 'III'
print(Solution().romanToInt(a))
