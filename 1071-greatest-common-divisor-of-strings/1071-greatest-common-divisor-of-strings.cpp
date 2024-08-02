using namespace std;


int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        
            
        
        int n1 = str1.size();
        int n2 = str2.size();
        
        
        if(str1 + str2 != str2 + str1){
             return "";
        }
           
        
        int gcd_length = gcd(n1, n2);
        
        
        string common_divisor;
        for(int i = 0; i<gcd_length; ++i){
            common_divisor += str1[i];
            
        }
        
        return common_divisor;
    }
};