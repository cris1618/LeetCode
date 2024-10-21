#include <string.h>

#define MAX_SEEN 100  // Adjust based on expected input size

char* seen[MAX_SEEN];
int seen_count = 0;

int is_in_seen(char* str) {
    for (int i = 0; i < seen_count; i++) {
        if (strcmp(seen[i], str) == 0) {
            return 1;
        }
    }
    return 0;
}

void add_to_seen(char* str) {
    seen[seen_count++] = strdup(str);  // Duplicate and add to seen
}

void remove_from_seen(char* str) {
    for (int i = 0; i < seen_count; i++) {
        if (strcmp(seen[i], str) == 0) {
            free(seen[i]);  // Free the duplicate string
            seen[i] = seen[seen_count - 1];  // Move last to current and decrease count
            seen_count--;
            return;
        }
    }
}

int backtrack(char* s, int start) {
    int len = strlen(s);
    if (start == len)
        return 0;

    int max_count = 0;
    for (int end = start + 1; end <= len; end++) {
        char* substring = (char*)malloc(end - start + 1);
        strncpy(substring, s + start, end - start);
        substring[end - start] = '\0';  // Null-terminate

        if (!is_in_seen(substring)) {
            add_to_seen(substring);
            int current_count = 1 + backtrack(s, end);
            max_count = current_count > max_count ? current_count : max_count;
            remove_from_seen(substring);
        }
        free(substring);  // Always free the allocated substring
    }
    
    return max_count;
}

int maxUniqueSplit(char* s) {
    int result = backtrack(s, 0);

    // Clean up any remaining dynamically allocated strings in seen
    for (int i = 0; i < seen_count; i++) {
        free(seen[i]);
    }
    seen_count = 0;  // Reset the seen count after use

    return result;
}
