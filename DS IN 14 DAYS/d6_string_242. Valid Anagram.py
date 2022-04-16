class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ######## Soln 3 ########
        
        ########## Soln 2 ###########
        s = sorted(s)
        t = sorted(t)
        return s==t
        
        ################# soln 1 ############
#         s_copy = s
#         for ch in t:
#             if ch in s_copy:
#                 s_copy = s_copy.replace(ch, "", 1)
        
#         if len(s)==len(t) and s_copy=="":
#             return True
#         else:
#             return False