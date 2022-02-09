"""
差的绝对值为 K 的数对数目
给你一个整数数组 nums 和一个整数 k ，请你返回数对 (i, j) 的数目，满足 i < j 且 |nums[i] - nums[j]| == k 。
"""


def count_k_difference(nums, k):
    ret = 0
    for idx, v in enumerate(nums):
        new_nums = nums[idx + 1:]
        tag = k + v
        _tag = v - k
        ret += (new_nums.count(tag) + new_nums.count(_tag))
    return ret


def count_k_difference_other(nums, k):
    ret = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                ret += 1
    return ret


if __name__ == '__main__':
    test_nums = [7, 7, 8, 3, 1, 2, 7, 2, 9, 5]
    test_k = 6

    ret = count_k_difference(test_nums, test_k)
    print(ret)

    ret = count_k_difference_other(test_nums, test_k)
    print(ret)
