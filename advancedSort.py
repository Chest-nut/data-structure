# -*- coding:utf-8 -*-

"""高级排序算法"""

import random
from copy import copy

from sorthelper import SortHelper
from basicSort import BasicSort

class AdvancedSort(SortHelper):
    """高级排序

    包括：希尔排序、两种归并排序、多种快速排序
    """

    def __init__(self):
        self.basic_sort = BasicSort()

    def shellSort(self, array, n=3):
        """希尔排序"""

        length = len(array)
        increment = length // n
        while increment >= 1:
            for i in range(increment):  # 分组数为increment
                # 每组内部进行插入排序
                for j in range(i+increment, length, increment):
                    tmp = array[j]
                    index = i   # 当前组的第一个数的索引
                    for k in range(j, increment-1, -increment):
                        if array[k-increment] > tmp:
                            array[k] = array[k-increment]
                        else:
                            index = k
                            break
                    array[index] = tmp
            increment = increment // n

        # 保证对任意的n值能够正确排序
        if increment is 0:
            self.basic_sort.insertion_sort1(array)


    def mergeSort1(self,array):
        """自顶向下的归并排序"""

        right = len(array)-1
        self.__mergeSort(array, 0, right)

    def mergeSort2(self,array):
        """自底而上的归并排序"""

        n = len(array)
        increment = 2
        while increment/2 < n:
            for i in range(0, n, increment):
                left = i; right = min(left+increment-1, n-1); mid = left + increment//2 -1
                if left is right:
                    break
                if mid >= right:
                    mid = (left+right) // 2
                if array[mid] >= array[mid+1]:
                    self.__merge(array, left, mid, right)
            increment *= 2

    def __merge(self, array, left, mid, right):
        """将数组的 [left,mid] 和 [mid+1,right] 两部分进行归并"""

        tmp = array[left:right+1]
        i = left
        j = mid + 1
        for k in range(left,right+1):
            if i > mid:
                array[k] = tmp[j-left]
                j += 1
            elif j > right:
                array[k] = tmp[i-left]
                i += 1
            elif tmp[i-left] < tmp[j-left]:
                array[k] = tmp[i-left]
                i += 1
            else:
                array[k] = tmp[j-left]
                j += 1

    def __mergeSort(self, array, left, right):
        """用自顶向下的归并排序算法
        对 [left,right] 范围进行归并排序
        """

        # 数组只有一个元素则不用进行排序
        # if left >= right:
        #     return

        # 优化
        if right-left < 16:
            self.basic_sort.insertion_sort1(array, left, right)
            return

        # 将数组分成前后两部分，各自进行归并排序后，再将两部分归并
        mid = (right+left) // 2
        self.__mergeSort(array, left, mid)
        self.__mergeSort(array, mid+1, right)
        if array[mid] >= array[mid+1]:  # 优化
            self.__merge(array, left, mid, right)


    def quickSort(self, array):
        """快速排序"""

        right = len(array) - 1
        self.__quickSort(array, 0, right)

    def __quickSort(self, array, left, right):
        """对 [left, right] 范围进行快速排序"""

        # if left >= right:
        #     return
        # 优化一：数组长度较小时使用插入排序
        if (right-left) <= 15:
            self.basic_sort.insertion_sort1(array, left, right)
            return
        p = self.__partition(array, left, right)
        self.__quickSort(array, left, p-1)
        self.__quickSort(array, p+1, right)

    def __partition(self, array, left, right):
        """将 [left, right] 范围的数进行partition操作，
        使得 array[left, p-1] < array[p] < array[p+1, right],
        并返回p的值
        """

        # 优化二:随机化快速排序
        # 取一个随机数作为标准，解决对于近乎有序数列排序时效率低的问题
        index = int(random.uniform(left, right))
        array[left], array[index] = array[index], array[left]

        v = array[left]
        # 要求：arr[left+1, j] < v < arr[j+1, i)
        j = left
        for i in range(left+1, right+1):
            if array[i] < v:
                array[i], array[j+1] = array[j+1], array[i]
                j += 1
        array[left], array[j] = array[j], array[left]
        return j

    def quickSort2(self, array):
        """快速排序2：双路快速排序

        解决对有大量重复数据的数组排序时递归太深的问题

        存在BUG:偶尔会出现程序一直运行，无结果
        """

        right = len(array) - 1
        self.__quickSort2(array, 0, right)

    def __quickSort2(self, array, left, right):
        """对 [left, right] 范围进行快速排序"""

        # if left >= right:
        #     return
        # 优化一：数组长度较小时使用插入排序
        if (right-left) <= 15:
            self.basic_sort.insertion_sort1(array, left, right)
            return
        p = self.__partition2(array, left, right)
        self.__quickSort2(array, left, p-1)
        self.__quickSort2(array, p+1, right)

    def __partition2(self, array, left, right):
        """将 [left, right] 范围的数进行partition操作，
        使得 array[left, p-1] < array[p] < array[p+1, right],
        并返回p的值
        """

        # 优化二:取一个随机数作为标准，解决对于近乎有序数列排序效率低的问题
        index = int(random.uniform(left, right))
        array[left], array[index] = array[index], array[left]
        v = array[left]

        # 优化三:双路快速排序
        # 解决了对有大量重复数据的数组排序时递归太深的问题
        # 要求：arr[left+1, i) < v < arr(j, right]
        # 偶尔退化
        i = left + 1
        j = right
        while True:
            # i <= right 必须在 array[i] < v 之前
            while i <= right and array[i] < v:i += 1
            while j >= left+1 and array[j] > v:j -= 1
            if j < i:break
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        array[left], array[j] = array[j], array[left]
        return j

    def my_quickSort(self, array):
        """快速排序"""

        right = len(array) - 1
        self.__my_quickSort(array, 0, right)

    def __my_quickSort(self, array, left, right):
        """对 [left, right] 范围进行快速排序"""

        if left >= right:
            return
        p = self.__my_partition(array, left, right)
        self.__my_quickSort(array, left, p-1)
        self.__my_quickSort(array, p+1, right)

    def __my_partition(self, array, left, right):
        """将 [left, right] 范围的数进行partition操作，
        使得 array[left, p-1] < array[p] < array[p+1, right],
        并返回p的值
        """

        index = int(random.uniform(left, right))
        array[left], array[index] = array[index], array[left]
        v = array[left]   # 选定第一个数位基准数
        i = 0             # i用于存放第一个比v大的数的索引，也就是索引大于i的数都比v大
        # 找出第一个比v大的数，索引值赋给i
        for j in range(left+1, right+1):
            if array[j] > v:
                i = j
                break
        # 如果i为0，说明没有数比v大
        if i is 0 :
            array[left], array[right] = array[right], array[left]
            return right
        # 如果i等于right，说明只有最后一个数比v大
        elif i is right:
            array[left], array[right-1] = array[right-1], array[left]
            return right-1

        # 找到有大于v的数之后，遍历之后的每个数，分成大于v和小于v两部分
        for e in range(i+1, right+1):
            if array[e] < v:
                array[e], array[i] = array[i], array[e]
                i += 1
        array[left], array[i-1] = array[i-1], array[left]
        return i-1


    def quickSort3Ways(self, array):
        """三路快速排序"""

        right = len(array) - 1
        self.__quickSort3Ways(array, 0, right)

    def __quickSort3Ways(self, array, left, right):
        """对 [left, right] 范围进行三路快速排序"""

        if (right-left) <= 15:
            self.basic_sort.insertion_sort1(array, left, right)
            return

        lt, gt = self.__partition3(array, left, right)
        self.__quickSort3Ways(array, left, lt-1) # 在lt换成lt-1之前性能极不稳定
        self.__quickSort3Ways(array, gt, right)

    def __partition3(self, array, left, right):
        """partition3操作"""

        index = int(random.uniform(left, right))
        array[left], array[index] = array[index], array[left]
        v = array[left]

        # # 要求：arr[left+1, lt] < arr[lt+1, i) = v < arr[gt, right]
        # # 偶尔退化
        # lt = left
        # i = lt + 1
        # gt = right + 1
        # while i < gt:
        #     if array[i] < v:
        #         array[i], array[lt+1] = array[lt+1], array[i]
        #         i += 1
        #         lt += 1
        #     elif array[i] > v:
        #         array[i], array[gt-1] = array[gt-1], array[i]
        #         gt -= 1
        #     else:
        #         i += 1
        # array[left], array[lt] = array[lt], array[left]
        # return lt, gt

        # 要求：arr[left+1, lt] < arr[lt+1, i) = v < arr[gt, right]
        # 偶尔退化
        lt = left
        i = lt + 1
        gt = right + 1
        while True:
            while i < gt and array[i] <= v:
                if array[i] is v:pass
                else:
                    array[i], array[lt+1] = array[lt+1], array[i]
                    lt += 1
                i += 1
            while i < gt and array[gt-1] > v:
                gt -= 1
            if gt <= i:
                break
            array[i], array[gt-1] = array[gt-1], array[i]
            gt -= 1
        array[left], array[lt] = array[lt], array[left]
        return lt, gt


if __name__ == '__main__':

    advanced_sort = AdvancedSort()

    n = 100000
    # array = []
    # 生成一个有大量重复元素的列表。
    # for i in range(n):
    #     array.append(random.choice(range(10)))

    # 生成一组包含n个乱序数字的列表
    array = random.sample(range(n),n)
    array_copy1 = copy(array)
    array_copy2 = copy(array)
    array_copy3 = copy(array)
    array_copy4 = copy(array)
    array_copy5 = copy(array)

    advanced_sort.test_sort(array, advanced_sort.shellSort, '希尔排序')
    advanced_sort.test_sort(array_copy1, advanced_sort.mergeSort1, '归并排序1')
    advanced_sort.test_sort(array_copy2, advanced_sort.quickSort, '快速排序1')
    advanced_sort.test_sort(array_copy3, advanced_sort.quickSort2, '双路快速排序')
    advanced_sort.test_sort(array_copy4, advanced_sort.my_quickSort, 'my快速排序')
    advanced_sort.test_sort(array_copy5, advanced_sort.quickSort3Ways, '三路快速排序')