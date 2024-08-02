using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        string merge = "";
        
        int i = 0;
        while(i < n1 || i < n2){
            if (i < n1){
               merge += word1[i]; 
            }
                
            if (i < n2){
                merge += word2[i];
            }
                
            i += 1;
        }
            
            
                
        return merge;
    }
};