class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        list_str = []
        
        for i in range(n):
            list_str.append(str(i+1))
        
        list_str.sort()
        list_lex = [int(x) for x in list_str]
        return list_lex