class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {} 
        h_length = 0
        for i in range(len(nums)):
            hash[nums[i]] = nums[i]
            if len(hash) <= h_length:
                return nums[i]
            h_length += 1
        