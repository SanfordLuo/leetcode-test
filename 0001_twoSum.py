"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def twoSum(nums, target):
    retList = []
    for index, num in enumerate(nums):
        if target - num in nums[(index + 1):]:
            retList.append(index)
            retList.append(index + 1 + nums[(index + 1):].index(target - num))
    return retList


def twoSumNew(nums, target):
    dict_new = {}
    for k, v in enumerate(nums):
        if target - v in dict_new:
            return dict_new[target - v], k
        else:
            dict_new[v] = k


print(twoSum(nums=[2, 7, 11, 15], target=9))
