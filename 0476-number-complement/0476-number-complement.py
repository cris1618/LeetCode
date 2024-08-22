class Solution:
    def findComplement(self, num: int) -> int:
        binary_str = bin(num)[2:]
        
        flipped_binary_str = ''.join('1' if b == '0' else '0' for b in binary_str)
        
        complement = int(flipped_binary_str, 2)
        
        return complement
        
            
            
            
        
        
        