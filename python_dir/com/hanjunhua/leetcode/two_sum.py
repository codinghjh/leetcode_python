class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        real_nums = list(nums)

        result = []
        for index, num in enumerate(real_nums):
            if real_nums.__contains__(target - num):
                if num == target - num:
                    if real_nums.count(num) > 1:
                        result.append(index)
                        result.append(real_nums.index(target - num, index + 1))
                        return result
                else:
                    result.append(index)
                    result.append(real_nums.index(target - num))
                    return result
