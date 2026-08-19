class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            num = target - nums[i]
            if num in nums and nums.index(num) != i:
                return sorted([i , nums.index(num)])
            i = i+1