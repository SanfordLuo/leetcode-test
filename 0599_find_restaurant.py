"""
599. 两个列表的最小索引总和
"""


def find_restaurant(list1, list2):
    tag = len(list1) + len(list2) - 2
    ret = []
    for idx, v in enumerate(list1):
        if v in list2:
            _tag = idx + list2.index(v)
            if _tag < tag:
                tag = _tag
                ret = [v]
            elif _tag == tag:
                ret.append(v)
    return ret


if __name__ == '__main__':
    test_a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    test_b = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    find_restaurant(test_a, test_b)
