class Solution:
    def countSeniors(self, details: List[str]) -> int:
        n = len(details)
        n_char = [len(s) for s in details]
        count = 0
        for i in range(n):
            if int(details[i][11]) * 10 + int(details[i][12]) > 60:
                count += 1
        return count
                
            