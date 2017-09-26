# -*- coding:utf-8 -*-

import random
from copy import copy

from basicSort import BasicSort
from advancedSort import AdvancedSort


if __name__ == '__main__':
    basic_sort = BasicSort()
    advanced_sort = AdvancedSort()

    n = 20000
    array = []
    # 生成一个有大量重复元素的列表。（为何本程序的三路快排大概率退化？）
    for i in range(n):
        array.append(random.choice(range(4)))

    # 生成一组包含n个乱序数字的列表
    # array = random.sample(range(n),n)
    array_copy1 = copy(array)
    array_copy2 = copy(array)
    array_copy3 = copy(array)
    array_copy4 = copy(array)
    array_copy5 = copy(array)

    # print(array_copy5)
    # advanced_sort.test_sort(array, advanced_sort.shellSort, '希尔排序')
    # advanced_sort.test_sort(array_copy1, advanced_sort.mergeSort1, '归并排序1')
    # advanced_sort.test_sort(array_copy2, advanced_sort.quickSort, '快速排序1')
    advanced_sort.test_sort(array_copy3, advanced_sort.quickSort2, '双路快速排序')
    # advanced_sort.test_sort(array_copy4, advanced_sort.my_quickSort, 'my快速排序')
    advanced_sort.test_sort(array_copy5, advanced_sort.quickSort3Ways, '三路快速排序')

    # print(array_copy5)