class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        nums1_point = 0
        nums2_point = 0
        ans = []
        
        while nums1_point < len(nums1) and nums2_point < len(nums2):
            
            if nums1[nums1_point]==nums2[nums2_point]:
                ans.append(nums1[nums1_point])
                nums1_point += 1
                nums2_point += 1
            elif nums1[nums1_point] < nums2[nums2_point]:
                nums1_point += 1
            else:
                nums2_point += 1
        return ans