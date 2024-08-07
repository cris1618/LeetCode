class Solution:
    def numberToWords(self, num: int) -> str:
        def threeDigitsToWords(num: int) -> str:
            below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",                               "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",                             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",                       "Ninety"]
            if num == 0:
                return ""
            elif num < 20:
                return below_20[num]
            elif num < 100:
                return tens[num // 10] + ("" if num % 10 == 0 else " " + below_20[num % 10])
            else:
                return below_20[num // 100] + " Hundred" + ("" if num % 100 == 0 else " " +                              threeDigitsToWords(num % 100))

        if num == 0:
            return "Zero"

        billions = num // 1000000000
        millions = (num // 1000000) % 1000
        thousands = (num // 1000) % 1000
        remainder = num % 1000

        result = ""
        if billions > 0:
            result += threeDigitsToWords(billions) + " Billion"
        if millions > 0:
            result += (" " if result else "") + threeDigitsToWords(millions) + " Million"
        if thousands > 0:
            result += (" " if result else "") + threeDigitsToWords(thousands) + " Thousand"
        if remainder > 0:
            result += (" " if result else "") + threeDigitsToWords(remainder)

        return result
        