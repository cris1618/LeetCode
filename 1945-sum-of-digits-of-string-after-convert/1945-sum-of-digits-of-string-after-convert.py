class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = len(s)
        
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)
            
        numeric_int = int(numeric_string)
        m = len(numeric_string)
        list_num = [int(x) for x in str(numeric_int)]
        
        
        while k > 0:
            sum_num = sum(list_num)
            k -= 1
            if k > 0:
                list_num = [int(x) for x in str(sum_num)]
        
        return sum_num
                
                