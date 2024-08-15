class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int n = bills.size();
        int money_bill_5 = 0;
        int money_bill_10 = 0;
        
        
        for(int i = 0; i<n; ++i){
            if(bills[i] == 5){
                money_bill_5 += 1;
            }    
            else if(bills[i] == 10){
                money_bill_10 += 1;
                if (money_bill_5 >= 1){
                  money_bill_5 -= 1;
                
                     
                }else{
                   return false;  
                }
                    
            }
                
            
            else{
                if(money_bill_5 >=1 && money_bill_10 >=1){
                    money_bill_5 -= 1;
                    money_bill_10 -= 1;
                }
                    
                else if(money_bill_5 >= 3){
                     money_bill_5 -= 3;
                } 
                   
                else{
                   return false; 
                }
                    
            }
                
                
        }
            
                
        return true;
    }
};