class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int sum = 0;
        for(int i = 0; i<m; i++){
            sum = rolls[i] + sum;
        }
        int remaining_sum = mean*(n + m) - sum;
        
        int max_sum = n * 6;
        int min_sum = n;
        
        if(remaining_sum > max_sum || remaining_sum < min_sum){
            return {}; 
        }
           
        
        int distribute_mean = int(remaining_sum/n);
        int mod = remaining_sum % n;
        
        vector<int> new_list(n, distribute_mean);
        for(int i = 0; i<mod; i++){
            new_list[i] += 1;
        }
            
        
        return new_list;
    }
};