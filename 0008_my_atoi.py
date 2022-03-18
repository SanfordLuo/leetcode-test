"""
8. 字符串转换整数 (atoi)
"""


def my_atoi(s):
    s = s.strip()
    ret = ''
    if len(s) == 0:
        return 0
    if s[0] in ('-', '+'):
        ret += s[0]
        s = s[1:]

    for _s in s:
        if _s.isdigit():
            ret += _s
        else:
            break
    try:
        if int(ret) < -2 ** 31:
            return -2 ** 31
        elif int(ret) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return int(ret)
    except Exception as e:
        return 0


if __name__ == '__main__':
    test_ret = my_atoi("+1")
    print(test_ret)
