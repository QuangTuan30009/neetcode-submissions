class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        # n = len(nums)
        # for i in range(n):
        #     for j in range (i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        