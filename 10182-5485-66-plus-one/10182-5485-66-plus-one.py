class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        str_num = ""
        for i in range(n):
            str_num += str(digits[i])
        num = int(str_num)
        
        int_result = num + 1
        str_result = str(int_result)
        res = []
        for i in range(len(str_result)):
            res.append(int(str_result[i]))
        
        return res
        
        