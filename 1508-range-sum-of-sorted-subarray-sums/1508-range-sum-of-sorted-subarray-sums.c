#include <stdio.h>
#include <stdlib.h>

#define MOD 1000000007

int cmpfunc(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}


int rangeSum(int* nums, int numsSize, int n, int left, int right) {
    int total_subarrays = (n * (n + 1)) / 2;
    int* subarray_sums = (int*)malloc(total_subarrays * sizeof(int));
    int index = 0;

    for (int i = 0; i < n; ++i) {
        int current_sum = 0;
        for (int j = i; j < n; ++j) {
            current_sum += nums[j];
            subarray_sums[index++] = current_sum;
        }
    }

    
    qsort(subarray_sums, total_subarrays, sizeof(int), cmpfunc);

    long long result = 0;

    
    for (int i = left - 1; i < right; ++i) {
        result = (result + subarray_sums[i]) % MOD;
    }

    free(subarray_sums);
    return (int)result;
}