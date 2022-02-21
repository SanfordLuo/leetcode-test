"""
717. 1 比特与 2 比特字符
有两种特殊字符：
第一种字符可以用一比特0表示
第二种字符可以用两比特（10或11）表示
给你一个以0结尾的二进制数组bits，如果最后一个字符必须是一个一比特字符，则返回true。
"""


def is_one_bit_character(bits):
    is_pass = False
    for idx, v in enumerate(bits):
        if is_pass:
            is_pass = False
            continue
        if v == 1:
            is_pass = True
        if idx + 1 == len(bits):
            if v == 0:
                return True
    return False


if __name__ == '__main__':
    test_bits_00 = [1, 0, 0]
    test_bits_01 = [1, 1, 1, 0]

    print(is_one_bit_character(test_bits_00))
    print(is_one_bit_character(test_bits_01))
