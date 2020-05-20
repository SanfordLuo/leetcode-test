"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
注意空字符串可被认为是有效字符串。

输入: "()" 输出: true
输入: "()[]{}" 输出: true
输入: "(]" 输出: false
输入: "([)]" 输出: false
输入: "{[]}" 输出: true
"""


def isValid(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    return s == ""


if __name__ == '__main__':
    s = "([)]"
    print(isValid(s))
