/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    int max_can = candies[0];
    for (int i = 1; i < candiesSize; ++i) {
        if (candies[i] > max_can) {
            max_can = candies[i];
        }
    }

    bool* result = (bool*)malloc(candiesSize * sizeof(bool));
    if (result == NULL) {
        // Handle memory allocation failure
        *returnSize = 0;
        return NULL;
    }

    for (int i = 0; i < candiesSize; ++i) {
        if (candies[i] + extraCandies >= max_can) {
            result[i] = true;
        } else {
            result[i] = false;
        }
    }

    *returnSize = candiesSize;
    return result;
}