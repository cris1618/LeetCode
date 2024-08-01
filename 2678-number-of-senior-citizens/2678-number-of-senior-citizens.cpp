using namespace std;

class Solution {
public:
    int countSeniors(vector<string>& details) {
        int n = details.size();
        int count = 0;
        for(int i = 0; i<n; ++i){
            int age = int(details[i][11] - '0') * 10 + int(details[i][12] - '0');
                if(age > 60){
                    count += 1;
                }
                
            }
        
                     
    return count;
    }
};