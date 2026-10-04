class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)-1):
        #     for j in range(1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n]=i
        return

