class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n1 = len(str1)
        n2 = len(str2)
        
        
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_length = gcd(n1, n2)
        
        return str1[:gcd_length]
            
        
        