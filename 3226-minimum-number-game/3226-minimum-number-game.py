class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 2):
            res.append(nums[i + 1])  # Player 2 goes first
            res.append(nums[i])      # then Player 1
        return res
