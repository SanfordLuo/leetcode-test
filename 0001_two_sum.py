"""
两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def two_sum(nums, target):
    ret_list = []
    for index, num in enumerate(nums):
        if target - num in nums[(index + 1):]:
            ret_list.append(index)
            ret_list.append(index + 1 + nums[(index + 1):].index(target - num))
    return ret_list


def two_sum_other(nums, target):
    dict_new = {}
    for k, v in enumerate(nums):
        if target - v in dict_new:
            return dict_new[target - v], k
        else:
            dict_new[v] = k


if __name__ == '__main__':
    test_nums = [2, 7, 11, 15]
    test_target = 9

    ret = two_sum(test_nums, test_target)
    print(ret)

    ret = two_sum_other(test_nums, test_target)
    print(ret)
