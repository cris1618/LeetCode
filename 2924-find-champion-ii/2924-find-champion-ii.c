int findChampion(int n, int** edges, int edgesSize, int* edgesColSize) {
        int in_degree[n];
        for(int i = 0; i<n; i++)
            in_degree[i] = 0;
    
        for(int i = 0; i<edgesSize; i++){
            in_degree[edges[i][1]] += 1;
        }
            
        int champ = -1;
        int champ_count = 0;
        
        for(int i = 0; i<n; i++){
            if(in_degree[i] == 0){
                champ_count++;
                champ = i;
            }
        }
            
        
        return champ_count > 1 ? -1 : champ;
            
}