class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        last = m + n - 1
        
        while i>=0 and j >=0 :
            if nums1[i] <= nums2[j]:
                nums1[last] = nums2[j]
                j -= 1
            elif nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            last -= 1
            
        while last >= 0 and j >= 0:
            nums1[last] = nums2[j]
            j, last = j-1, last-1
            
        print(nums1)
        
        
        ### unoptimized solution
#         i = m
#         j = 0
#         while i < m+n:
#             nums1[i] = nums2[j]
#             i += 1
#             j += 1
        
#         nums1.sort()