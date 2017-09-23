# -*- coding:utf-8 -*-

import random
from copy import copy

from basicSort import BasicSort


if __name__ == '__main__':
    basic_sort = BasicSort()

    array = random.sample(range(5000),5000)  # 生成一组包含5000个乱序数字的列表
    array_copy = copy(array)    # 拷贝一份一样的乱序数组
    array_copy2 = copy(array)
    array_copy3 = copy(array)
    array_copy4 = copy(array)
    array_copy5 = copy(array)

    basic_sort.test_sort(array, basic_sort.insertion_sort_py, 'py插入排序')
    basic_sort.test_sort(array_copy, basic_sort.insertion_sort, '未优化插入排序')
    basic_sort.test_sort(array_copy2, basic_sort.insertion_sort1, '已优化插入排序')
    basic_sort.test_sort(array_copy3, basic_sort.selection_sort, '选择排序')
    basic_sort.test_sort(array_copy4, basic_sort.bubble_sort, '冒泡排序')
    basic_sort.test_sort(array_copy5, basic_sort.shell_sort, '希尔排序')

