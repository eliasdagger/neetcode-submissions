class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -a
            front, rear = i + 1, len(nums) - 1

            while front < rear:
                current_sum = nums[front] + nums[rear]
                
                if current_sum == target:
                    res.append([a, nums[front], nums[rear]])
                    
                    front += 1
                    rear -= 1
                    
                    while front < rear and nums[front] == nums[front - 1]:
                        front += 1
                        
                    while front < rear and nums[rear] == nums[rear + 1]:
                        rear -= 1

                elif current_sum > target:
                    rear -= 1
                else:
                    front += 1
                    
        return res