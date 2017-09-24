# -*- coding:utf-8 -*-

import random
from copy import copy

from basicSort import BasicSort
from advancedSort import AdvancedSort


if __name__ == '__main__':
    basic_sort = BasicSort()
    advanced_sort = AdvancedSort()

    n = 30000
    array = random.sample(range(n),n)  # 生成一组包含n个乱序数字的列表
    array_copy1 = copy(array)    # 拷贝一份一样的乱序数组
    array_copy2 = copy(array)
    array_copy3 = copy(array)
    array_copy4 = copy(array)
    array_copy5 = copy(array)
    array_copy6 = copy(array)
    array_copy7 = copy(array)

    # basic_sort.test_sort(array, basic_sort.insertion_sort_py, 'py插入排序')
    # basic_sort.test_sort(array_copy1, basic_sort.insertion_sort, '未优化插入排序')
    # basic_sort.test_sort(array_copy2, basic_sort.insertion_sort1, '已优化插入排序')
    # basic_sort.test_sort(array_copy3, basic_sort.selection_sort, '选择排序')
    # basic_sort.test_sort(array_copy4, basic_sort.bubble_sort, '冒泡排序')

    advanced_sort.test_sort(array_copy5, advanced_sort.shell_sort, '希尔排序')
    advanced_sort.test_sort(array_copy6, advanced_sort.mergeSort1, '归并排序1')
    advanced_sort.test_sort(array_copy7, advanced_sort.mergeSort2, '归并排序2')