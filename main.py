# -*- coding:utf-8 -*-

import random
from copy import copy

from sortalgorithm import SortHelper


if __name__ == '__main__':
    sort_ = SortHelper()

    array = random.sample(range(5000),5000)  # 生成一组包含5000个乱序数字的列表
    array_copy = copy(array)    # 拷贝一份一样的乱序数组
    array_copy2 = copy(array)
    array_copy3 = copy(array)
    array_copy4 = copy(array)
    array_copy5 = copy(array)

    sort_.test_sort(array, sort_.insertion_sort_py, 'py插入排序')
    sort_.test_sort(array_copy, sort_.insertion_sort, '未优化插入排序')
    sort_.test_sort(array_copy2, sort_.insertion_sort1, '已优化插入排序')
    sort_.test_sort(array_copy3, sort_.selection_sort, '选择排序')
    sort_.test_sort(array_copy4, sort_.bubble_sort, '冒泡排序')
    sort_.test_sort(array_copy5, sort_.shell_sort, '希尔排序')

