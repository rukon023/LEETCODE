class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_val = curr_max = nums[0]
        for i in range(1, len(nums)):
            curr_val = nums[i]
            curr_max = max(curr_val, curr_max + curr_val)
            max_val = max(max_val, curr_max)
        return max_val