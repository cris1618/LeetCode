class Solution:
    def strangePrinter(self, s: str) -> int:
        # Remove consecutive duplicates
        s = "".join(char for char, _ in itertools.groupby(s))
        n = len(s)
        
        # Memoization dictionary
        memo = {}
        
        # Helper function to find the minimum turns for the substring s[start:end]
        def _minimum_turns(start, end):
            if start > end:
                return 0
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            # Start with the assumption that the minimum turns are just to print from start to end
            min_turns = 1 + _minimum_turns(start + 1, end)
            
            # Iterate through the substring
            for k in range(start + 1, end + 1):
                if s[k] == s[start]:
                    turns_with_match = _minimum_turns(start, k - 1) + _minimum_turns(k + 1, end)
                    min_turns = min(min_turns, turns_with_match)
                
            memo[(start, end)] = min_turns
            return min_turns
        
        # Call the helper function starting from the full string
        return _minimum_turns(0, n - 1)
                    
            
                
                
                
            
            
        