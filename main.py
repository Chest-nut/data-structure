# -*- coding:utf-8 -*-

import random
from copy import copy

from basicSort import BasicSort
from advancedSort import AdvancedSort


if __name__ == '__main__':
    basic_sort = BasicSort()
    advanced_sort = AdvancedSort()

    n = 100000
    # array = []
    # for i in range(400000):
    #     array.append(random.sample(range(10),1)[0])
    array = random.sample(range(n),n)  # 生成一组包含n个乱序数字的列表
    array_copy1 = copy(array)    # 拷贝一份一样的乱序数组
    array_copy2 = copy(array)
    array_copy3 = copy(array)
    array_copy4 = copy(array)
    array_copy5 = copy(array)

    # print(array_copy5)
    advanced_sort.test_sort(array, advanced_sort.shellSort, '希尔排序')
    advanced_sort.test_sort(array_copy1, advanced_sort.mergeSort1, '归并排序1')
    advanced_sort.test_sort(array_copy2, advanced_sort.quickSort, '快速排序1')
    advanced_sort.test_sort(array_copy3, advanced_sort.quickSort2, '双路快速排序')
    advanced_sort.test_sort(array_copy4, advanced_sort.my_quickSort, 'my快速排序')
    advanced_sort.test_sort(array_copy5, advanced_sort.quickSort3Ways, '三路快速排序')

    # print(array_copy5)