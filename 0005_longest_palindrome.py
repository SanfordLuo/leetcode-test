"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：   输入: "babad" 输出: "bab"   注意: "aba" 也是一个有效答案。
示例 2：   输入: "cbbd"  输出: "bb"
"""


def longest_palindrome(s):
    if s == s[::-1]:
        return s
    for i in range(1, len(s)):
        a, b = 0, len(s) - i
        while b <= len(s):
            if s[a:b] == s[a:b][::-1]:
                return s[a:b]
            a, b = a + 1, b + 1


if __name__ == '__main__':
    s = "babad"
    print(longest_palindrome(s))
