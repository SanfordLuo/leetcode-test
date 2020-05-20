"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
输入: 121 输出: true
输入: -121 输出: false
"""


def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False


print(isPalindrome(x=121))
