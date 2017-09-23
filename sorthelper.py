# -*- coding:utf-8 -*-

"""
排序助手
"""

import time


class SortHelper(object):
    """排序类的基类"""

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
