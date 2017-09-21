# -*- coding:utf-8 -*-

"""
排序算法
"""

import random
import time
from copy import copy, deepcopy

class Sort(object):

    def __init__(self):
        self.array = []


    def insertion_sort1(self, array):
        """
        n从2开始，取第n个数，将其依次与第1到第n-1个数进行比较，
        当遇见有一个数比这个数大时，将这个数pop出，
        并insert到那个比它大的数的位置。
        """

        self.array = array
        count = 0
        for i in range(1,len(self.array)):
            for j in range(i):
                count += 1
                if self.array[i] <= self.array[j]:
                    tmp = self.array.pop(i)
                    self.array.insert(j, tmp)
                    break
        print(count)


    def insertion_sort2(self, array):
        """
        n从2开始，取第n个数，将其和前一个数比较，
        如果比前一个数小，则互换位置，然后再和前一个数比较，以此类推，
        直到比前一个数大为止
        """

        self.array = array
        count = 0
        for i in range(1, len(self.array)):
            for j in range(i, 0, -1):
                count += 1
                if self.array[j] < self.array[j-1]:
                    self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                else:
                    break
        print(count)


    def view(self):
        print(self.array)


if __name__ == '__main__':
    # 比较两种插入算法的效率

    sort_ = Sort()
    array = random.sample(range(100000), 5000)
    # array = random.sample(range(50), 5)
    array_copy = copy(array)    # 拷贝一份一样的乱序数组

    time1 = time.time()
    sort_.insertion_sort1(array)
    # sort_.view()
    time2 = time.time()
    sort_.insertion_sort2(array_copy)
    # sort_.view()
    time3 = time.time()
    print(time2 - time1)    # 1.077385425567627s
    print(time3 - time2)    # 3.2283499240875244s