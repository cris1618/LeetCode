#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        int m = points[0].size();
        
        // DP array to store the maximum points for the current row
        vector<long long> dp(points[0].begin(), points[0].end());
        
        for (int i = 1; i < n; ++i) {
            // Arrays to store max values from left to right and right to left
            vector<long long> left_max(m, 0), right_max(m, 0);
            
            // Fill the left max array
            left_max[0] = dp[0];
            for (int j = 1; j < m; ++j) {
                left_max[j] = max(left_max[j - 1] - 1, dp[j]);
            }
            
            // Fill the right max array
            right_max[m - 1] = dp[m - 1];
            for (int j = m - 2; j >= 0; --j) {
                right_max[j] = max(right_max[j + 1] - 1, dp[j]);
            }
            
            // Update the dp array for the current row
            for (int j = 0; j < m; ++j) {
                dp[j] = points[i][j] + max(left_max[j], right_max[j]);
            }
        }
        
        // Return the maximum value in dp array
        return *max_element(dp.begin(), dp.end());
    }
};