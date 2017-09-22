# -*- coding:utf-8 -*-

"""
排序算法
"""

import time


class SortHelper(object):

    def __init__(self):
        self.array = []

    def test_sort(self, array, sort_method, sort_name='排序'):
        start_time = time.time()
        sort_method(array)
        end_time = time.time()
        assert self.is_sorted(array)
        print('%s耗时：%fs'%(sort_name, end_time - start_time) )

    def insertion_sort1(self, array):
        """python动态语言特性实现的插入排序：

        n从2开始，取第n个数，将其依次与第1到第n-1个数进行比较，
        当遇见有一个数比这个数大时，将这个数pop出，
        并insert到那个比它大的数的位置。
        """

        self.array = array
        for i in range(1, len(self.array)):
            for j in range(i):
                if self.array[i] <= self.array[j]:
                    tmp = self.array.pop(i)
                    self.array.insert(j, tmp)
                    break


    def insertion_sort2(self, array):
        """传统插入排序：

        n从2开始，取第n个数，将其和前一个数比较，
        如果比前一个数小，则互换位置，然后再和前一个数比较，以此类推，
        直到比前一个数大为止
        """

        self.array = array
        for i in range(1, len(self.array)):
            for j in range(i, 0, -1):
                if self.array[j] < self.array[j-1]:
                    self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                else:
                    break


    def selection_sort(self, array):
        """选择排序"""

        n = len(array)
        for i in range(n-1):
            minIndex = i
            for j in range(i+1, n):
                if array[minIndex]  > array[j]:
                    minIndex, j = j, minIndex
            array[minIndex], array[i] = array[i], array[minIndex]
        return array

    def is_sorted(self, array):
        """判断是否排序正确"""
        n = len(array)
        for i in range(n-1):
            if array[i] > array[i+1]:
                return False
        return True