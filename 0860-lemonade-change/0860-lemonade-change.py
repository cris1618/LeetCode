class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        money_bill_5 = 0
        money_bill_10 = 0
        
        
        
        for i in range(n):
            if bills[i] == 5:
                money_bill_5 += 1
                
                
            elif bills[i] == 10:
                money_bill_10 += 1
                if money_bill_5 >= 1:
                    money_bill_5 -= 1
                else:
                    return False
            
            else:
                
                if money_bill_5 >=1 and money_bill_10 >=1:
                    money_bill_5 -= 1
                    money_bill_10 -= 1
                elif money_bill_5 >= 3:
                    money_bill_5 -= 3
                else:
                    return False
                
        return True  
            
            
        
        