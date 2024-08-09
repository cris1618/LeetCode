#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int nrow = grid.size();
        int ncol = grid[0].size();
        
        int count = 0;
        for(int i = 0; i < nrow - 2; ++i){
            for(int j = 0; j < ncol - 2; ++j){
                if(is_magic_square(grid, i, j)){
                    count += 1;
                }
            }  
        }      
        return count;
    }
    
private:
    bool is_magic_square(vector<vector<int>>& grid, int start_row, int start_col) {
        set<int> nums;
        vector<int> sums;

        for(int i = 0; i < 3; ++i){
            for(int j = 0; j < 3; ++j){
                int num = grid[start_row + i][start_col + j];
                if(num < 1 || num > 9){
                    return false;
                } 
                nums.insert(num);
            }
        }

        if(nums.size() != 9) {
            return false;
        }

        for (int i = 0; i < 3; ++i) {  
            int row_sum = 0;
            for (int j = 0; j < 3; ++j) {  
                row_sum += grid[start_row + i][start_col + j];
            }
            sums.push_back(row_sum);
        }
        
        for (int i = 0; i < 3; ++i) {  
            int col_sum = 0;
            for (int j = 0; j < 3; ++j) {  
                col_sum += grid[start_row + j][start_col + i];
            }
            sums.push_back(col_sum);
        }

        int diag1_sum = grid[start_row][start_col] + grid[start_row + 1][start_col + 1] + grid[start_row + 2][start_col + 2];
        int diag2_sum = grid[start_row][start_col + 2] + grid[start_row + 1][start_col + 1] + grid[start_row + 2][start_col];

        sums.push_back(diag1_sum);
        sums.push_back(diag2_sum);

        bool all_equal = true;
        for (int s : sums) {
            if (s != sums[0]) {
                all_equal = false;
                break;
            }
        }
        return all_equal;
    }
};
