class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = {}
        
        for i in range(len(s)):
            if s[i] in count_dict:
                count_dict[s[i]] += 1
            else: 
                count_dict[s[i]] = 1
        
        for i in range(len(s)):
            if count_dict[s[i]] == 1:
                return i
        return -1