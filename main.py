# -*- coding:utf-8 -*-

import time
import random
from copy import copy, deepcopy

from sortalgorithm import SortHelper


if __name__ == '__main__':
    sort_ = SortHelper()

    array = random.sample(range(5000), 5000)  # 生成一组包含5000个乱序数字的列表
    array_copy = copy(array)    # 拷贝一份一样的乱序数组
    array_copy2 = copy(array)

    sort_.test_sort(array, sort_.insertion_sort1, '插入排序1')
    sort_.test_sort(array_copy, sort_.insertion_sort2, '插入排序2')
    sort_.test_sort(array_copy2, sort_.selection_sort, '选择排序')

