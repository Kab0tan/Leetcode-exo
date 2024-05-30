class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        trans = ""
        j = 0
        while num > 0:
            for i in range(num//integers[j]):
                trans+= roman[j]
                num-= integers[j] 
            j+=1
        return trans

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         dic = {
#             1000: 'M',
#             900: 'CM',
#             500: 'D',
#             400: 'CD',
#             100: 'C',
#             90: 'XC',
#             50: 'L',
#             40: 'XL',
#             10: 'X',
#             9: 'IX',
#             5: 'V',
#             4: 'IV',
#             1: 'I'
#         }

#         trans = ""

#         for i in dic.keys():
#             if num // i != 0:
#                 div = num // i
#                 num = num % i
#                 trans+= dic[i]*div


#         return trans
