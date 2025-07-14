class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff = {}
        res = []
        for i in range(len(nums)):
            d = target - nums[i]
            if d in diff:
                res.append(i)
                res.append(diff[d])
                return res
            else:
                diff[nums[i]] = i
