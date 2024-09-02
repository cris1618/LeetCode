using namespace std;

class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int n = chalk.size();
        long long int total_chalk = 0;
        for(int i = 0; i<n; i++){
            total_chalk += chalk[i];
        }
        k = k % total_chalk;
        
        
        int index = 0;
        while(1){
            if (k < chalk[index]){
                return index;
            }
            k -= chalk[index];
            index = (index + 1) % n;
        }
            
        
        return index;   
    }
};