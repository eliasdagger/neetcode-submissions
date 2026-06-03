class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        rear = len(numbers) - 1
        while head < rear:
            if numbers[head] + numbers[rear] == target:
                res = [head + 1, rear + 1]
                return res

            if numbers[head] + numbers[rear] > target:
                rear -= 1
            elif numbers[head] + numbers[rear] < target:
                head += 1
        return []
        