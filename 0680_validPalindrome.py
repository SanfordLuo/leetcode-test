"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
示例 1: 输入: "aba" 输出: True
示例 2: 输入: "abca" 输出: True 解释: 你可以删除c字符。
字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""


def validPalindrome_me(s):
    if s == s[::-1]:
        return True
    else:
        for i in range(len(s)):
            new_s = s[:i] + s[i + 1:]
            if new_s == new_s[::-1]:
                return True
        return False


def validPalindrome(s):
    if s == s[::-1]:
        return True
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i, j = i + 1, j - 1
        else:
            a = s[i + 1:j + 1]
            b = s[i:j]
            return a == a[::-1] or b == b[::-1]


if __name__ == '__main__':
    s = "cbbcc"

    print(validPalindrome(s))
