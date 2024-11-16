/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultsArray(int* nums, int numsSize, int k, int* returnSize) {
         // Validate inputs
        if (numsSize < k || k <= 0) {
            *returnSize = 0;
            return NULL;  // Return NULL if no valid result can be computed
        }

        // Set return size
        *returnSize = numsSize - k + 1;

        // Allocate memory for result array
        int* result = malloc((*returnSize) * sizeof(int));
        if (!result) {
            *returnSize = 0;  // Handle allocation failure
            return NULL;
        }
        
        for(int start = 0; start<numsSize - k + 1; start++){
            bool is_consecutive_and_ordered = true;
            
            for(int index = start; index<start+k-1; index++){
                if(nums[index + 1] != nums[index] + 1){
                    is_consecutive_and_ordered = false;
                    break;
                }       
            }   
            if(is_consecutive_and_ordered)
                result[start] = nums[start + k - 1];
            else
                result[start] = -1;
        }
            
                    
        return result;      
}