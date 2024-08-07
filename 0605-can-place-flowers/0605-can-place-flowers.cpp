class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        int m = flowerbed.size();
        
        for(int i = 0; i < m; ++i) {
            if(flowerbed[i] == 0) {
                bool prev = (i == 0) || (flowerbed[i - 1] == 0);
                bool next = (i == m - 1) || (flowerbed[i + 1] == 0);
                
                if(prev && next) {
                    flowerbed[i] = 1;
                    count += 1;
                    
                    
                    i++;
                }
            }
            
            if (count >= n) {
                return true;
            }
        }
        
        return false;
    }

};