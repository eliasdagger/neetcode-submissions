class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        res = 0
        while r < len(s):
            if len(set(s[l:r+1])) > len(set(s[l:r])):
                r += 1
                print(f"increasing window {l} - {r}")
            else:
                l += 1
                print(f"shifting window {l} - {r}")
            res = max(res, r - l)

        return res

            

        