# -*- coding:utf-8 -*-

"""
排序算法
"""

import time


class SortHelper(object):

    def test_sort(self, array, sort_method, sort_name='排序'):
        """测试排序耗时"""

        start_time = time.time()
        sort_method(array)
        end_time = time.time()
        assert self.is_sorted(array)    # 判断排序是否正确
        print('%s耗时：%fs'%(sort_name, (end_time - start_time)) )


    def is_sorted(self, array):
        """判断是否排序正确"""

        n = len(array)
        for i in range(n-1):
            if array[i] > array[i+1]:
                return False
        return True


    def insertion_sort(self, array):
        """传统插入排序：

        n从2开始，取第n个数，将其和前一个数比较，
        如果比前一个数小，则互换位置，然后再和前一个数比较，以此类推，
        直到比前一个数大为止
        """

        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    break


    def insertion_sort1(self, array):
        """经过优化的传统插入排序"""

        for i in range(1, len(array)):
            # 算法优化如下：
            tmp = array[i]
            index = 0
            for j in range(i, 0, -1):
                if array[j-1] > tmp:
                    array[j] = array[j-1]
                else:
                    index = j
                    break
            array[index] = tmp


    def insertion_sort_py(self, array):
        """python动态语言特性实现的插入排序：

        n从2开始，取第n个数，将其依次与第1到第n-1个数进行比较，
        当遇见一个数比它大时，说明它就应该插入到比它大这个数之前，
        只需将其pop出，然后insert到那个比它大的数的位置。
        """

        for i in range(1, len(array)):
            for j in range(i):
                if array[i] <= array[j]:
                    tmp = array.pop(i)
                    array.insert(j, tmp)
                    break


    def selection_sort(self, array):
        """选择排序"""

        n = len(array)
        for i in range(n-1):
            minIndex = i
            for j in range(i+1, n):
                if array[minIndex]  > array[j]:
                    minIndex = j
            if minIndex is not i:
                array[minIndex], array[i] = array[i], array[minIndex]


    def bubble_sort(self, array):
        """冒泡排序"""

        n = len(array)
        flag = True     # flag 用于优化当后面的数列已经有序的情况
        for i in range(n):
            if flag:
                flag = False    # 如果本次循环结束flag仍为False，说明后续数列已经有序，下次循环不再进行
                for j in range(n-1, i, -1):
                    if array[j-1] > array[j]:
                        array[j-1], array[j] = array[j], array[j-1]
                        flag = True
            else:
                break


    def shell_sort(self, array, n=4):
        """希尔排序"""

        length = len(array)
        increment = length // n
        while increment >= 1:
            for i in range(increment):  # 分组数为increment
                # 每组内部进行插入排序
                for j in range(i+increment, length, increment):
                    tmp = array[j]
                    index = i
                    for k in range(j, increment-1, -increment):
                        if array[k-increment] > tmp:
                            array[k] = array[k-increment]
                        else:
                            index = k
                            break
                    array[index] = tmp
            increment = increment // n

