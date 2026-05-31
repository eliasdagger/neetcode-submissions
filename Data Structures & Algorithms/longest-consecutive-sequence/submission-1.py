class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = 0
        n = sorted(set(nums))
        for i in range(len(n)):
            c2 = 1
            for j in range(i + 1, len(n)):
                if n[j] == n[j - 1] + 1:
                    c2 +=1
                else:
                    break
            if c2 > c:
                c = c2
        return c

            
            

        

            
            
            

        