bool rotateString(char* s, char* goal) {
    // Check if the lengths of s and goal are different
    size_t len_s = strlen(s);
    size_t len_goal = strlen(goal);
    if (len_s != len_goal) {
        return false;
    }
    
    // Allocate memory for the doubled string
    char* doubled_string = malloc(len_s * 2 + 1); // +1 for the null terminator
    if (!doubled_string) {
        perror("Failed to allocate memory");
        return false;
    }
    
    // Create the doubled string by concatenating s with itself
    strcpy(doubled_string, s);
    strcat(doubled_string, s);
    
    // Check if goal is a substring of the doubled string
    bool result = strstr(doubled_string, goal) != NULL;
    
    // Free the allocated memory
    free(doubled_string);
    
    return result;
}