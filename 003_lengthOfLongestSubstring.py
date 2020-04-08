"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


def lengthOfLongestSubstring(s):
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
    print(lengthOfLongestSubstring(s))
