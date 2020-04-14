"""
所有输入只包含小写字母 a-z,查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower", "flow", "flight"]
输出: "fl"

示例 2:
输入: ["dog", "racecar", "car"]
输出: ""
解释: 输入不存在公共前缀。

[m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
"""


def longestCommonPrefix(strs):
    if not strs:
        return ""
    str = min(strs, key=len)
    for i in range(len(str)):
        s = str[:i + 1]
        if not all([s == text[:i + 1] for text in strs]):
            return str[:i]
    return str


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    # strs = ["fl", "flow", "flight"]
    # strs = ["ca", "a"]
    print(longestCommonPrefix(strs))
