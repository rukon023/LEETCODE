class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_dict = {}
        
        for i in range(len(nums)):
            k = target-nums[i]
            if k in check_dict:
                return [check_dict[k], i]
            else:
                check_dict[nums[i]] = i
        return False