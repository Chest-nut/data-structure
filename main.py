# -*- coding:utf-8 -*-

import time
import random
from copy import copy, deepcopy

from sortalgorithm import Sort


if __name__ == '__main__':
    sort_ = Sort()

    # # 比较两种插入算法的效率：
    #
    # array = random.sample(range(5000), 5000)  # 生成一组包含5000个乱序数字的列表
    # # array = random.sample(range(5), 5)
    # array_copy = copy(array)    # 拷贝一份一样的乱序数组
    #
    # time1 = time.time()
    # sort_.insertion_sort1(array)
    # # sort_.view()
    # time2 = time.time()
    # sort_.insertion_sort2(array_copy)
    # # sort_.view()
    # time3 = time.time()
    # print(time2 - time1)    # 1.077385425567627s
    # print(time3 - time2)    # 3.2283499240875244s

    # 选择排序算法部分：
    array = random.sample(range(5000), 5000)
    # print(array)
    time1 = time.time()
    arr = sort_.selection_sort(array)
    time2 = time.time()
    # print(arr)
    print(time2 - time1)