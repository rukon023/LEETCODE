class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for ch in ransomNote:
            if ch in magazine:
                magazine = magazine.replace(ch, "", 1)
            else:
                return False
        return True
        
        ######################## old submission ##############
#         cnt_dict = {}
        
#         for i in range(len(magazine)):
#             if magazine[i] in cnt_dict:
#                 cnt_dict[magazine[i]] += 1
#             else:
#                 cnt_dict[magazine[i]] = 1
        
#         for i in range(len(ransomNote)):
#             if ransomNote[i] in cnt_dict:
#                 if cnt_dict[ransomNote[i]] == 0:
#                     return False
#                 else:
#                     cnt_dict[ransomNote[i]] -= 1
#             else:
#                 return False
#         return True