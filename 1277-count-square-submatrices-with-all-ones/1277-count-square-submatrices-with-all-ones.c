int min(int a, int b){
    return (a<b) ? a : b;
}

int solve(int i,int j, int matrixSize, int matrixColSize, int** grid, int** dp){
    if((i >= matrixSize) || (j >= (matrixColSize)))
            return 0;
        if(grid[i][j] == 0)
            return 0;
        if(dp[i][j] != -1)
            return dp[i][j];
        
        int right = solve(i, j+1, matrixSize, matrixColSize, grid, dp);
        int diagonal = solve(i+1, j+1, matrixSize, matrixColSize, grid, dp);
        int below = solve(i+1, j, matrixSize, matrixColSize, grid, dp);
        dp[i][j] = 1 + min(right, min(diagonal, below));
        return dp[i][j];
}
        

int countSquares(int** matrix, int matrixSize, int* matrixColSize) {
    int ans = 0;
        int **dp = malloc(matrixSize * sizeof(int*));
    for (int i = 0; i < matrixSize; i++) {
        dp[i] = malloc(*matrixColSize * sizeof(int));
        for (int j = 0; j < *matrixColSize; j++)
            dp[i][j] = -1;
    }
        
    
        for(int i=0; i<matrixSize; i++){
            for(int j=0; j<*matrixColSize; j++)
                ans += solve(i,j, matrixSize, *matrixColSize, matrix, dp);
        }
         for (int i = 0; i < matrixSize; i++) {
        free(dp[i]);
    }
    free(dp);  
                
        return ans;  
    
}