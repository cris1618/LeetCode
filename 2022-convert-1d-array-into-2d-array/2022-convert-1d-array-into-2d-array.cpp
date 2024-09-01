class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
     // Check if it is possible to form an m x n 2D array
        if (m * n != original.size()) {
            // If not, return an empty 2D array
            return {};
        }

        // Initialize the result 2D array with m rows and n columns
        vector<vector<int>> resultArray(m, vector<int>(n));
        
        int index = 0;
        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                resultArray[i][j] = original[index];
                index += 1;
            }
                
        }
            
        
        return resultArray;
        
        
    }
};