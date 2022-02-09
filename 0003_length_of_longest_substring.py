"""
无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

输入: "abcabcbb"
输出: 3   "abc"

输入: "bbbbb"
输出: 1   "b"

输入: "pwwkew"
输出: 3   "wke"
"""


def length_of_longest_substring(s):
    temp = 0
    my_dict = {}
    start = 0
    for i, num in enumerate(s):
        if num in my_dict and start <= my_dict[num]:
            start = my_dict[num] + 1
        temp = max(i - start + 1, temp)
        my_dict[num] = i
    return temp


if __name__ == '__main__':
    s = "abcabcbb"

    ret = length_of_longest_substring(s)
    print(ret)
