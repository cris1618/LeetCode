#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* invertAndReverse(const char* str, int length) {
    char* inverted = (char*)malloc(length + 1); // Allocate memory for the inverted string
    if (!inverted) return NULL;

    for (int i = 0; i < length; i++) {
        inverted[length - i - 1] = str[i] == '0' ? '1' : '0'; // Invert and reverse simultaneously
    }
    inverted[length] = '\0'; // Null-terminate the string
    return inverted;
}

char findKthBit(int n, int k) {
    char* sequence = (char*)malloc(2); // Initially allocate memory for the sequence
    if (!sequence) return '\0';

    strcpy(sequence, "0"); // Start with "0"
    int currentLength = 1;

    for (int i = 1; i < n; i++) {
        if (k <= currentLength) {
            break; // If k is within the current length, no need to continue
        }

        // Expand sequence with "1"
        sequence = (char*)realloc(sequence, currentLength * 2 + 2); // Double the space plus one for '1' and null character
        if (!sequence) return '\0';

        sequence[currentLength] = '1'; // Append '1'
        currentLength++;

        char* inverted = invertAndReverse(sequence, currentLength - 1);
        if (!inverted) {
            free(sequence);
            return '\0';
        }

        // Append the inverted and reversed string
        strcpy(sequence + currentLength, inverted); // Append inverted to sequence
        currentLength += strlen(inverted); // Update length
        free(inverted); // Free the inverted string
    }

    char result = sequence[k - 1]; // Get the k-th bit
    free(sequence); // Free the allocated memory for sequence
    return result;
}

