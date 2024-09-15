class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        character_map = [0]*26
        character_map[ord("a") - ord("a")] = 1
        character_map[ord("e") - ord("a")] = 2
        character_map[ord("i") - ord("a")] = 4
        character_map[ord("o") - ord("a")] = 8
        character_map[ord("u") - ord("a")] = 16
        mp = [-1]*32
        longest_substring = 0
        for i in range(len(s)):
            prefixXOR ^= character_map[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longest_substring = max(longest_substring, i-mp[prefixXOR])
        return longest_substring