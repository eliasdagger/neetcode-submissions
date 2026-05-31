class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        # find two indexs that == 7
        
        for i in range(len(nums)):
            
            missing_var = target - nums[i]
            
            if missing_var in dic and dic[missing_var] != i:
                return [i, dic[missing_var]]
        return []