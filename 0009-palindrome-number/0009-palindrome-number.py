class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num_str = str(x)
        
        
        left, right = 0, len(num_str) - 1
        
       
        while left < right:
            if num_str[left] != num_str[right]:
                return False
            left += 1
            right -= 1
        
        return True
                    
        