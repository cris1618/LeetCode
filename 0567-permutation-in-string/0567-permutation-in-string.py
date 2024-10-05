class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_count = Counter(s1)
        window_count = Counter()

        for i in range(m):
            # Add one more letter on the right side of the window
            window_count[s2[i]] += 1
            # Remove one letter from the left side of the window if needed
            if i >= n:
                if window_count[s2[i - n]] == 1:
                    del window_count[s2[i - n]]
                else:
                    window_count[s2[i - n]] -= 1
            # Compare window with s1_count
            if window_count == s1_count:
                return True
        return False

            
        
        