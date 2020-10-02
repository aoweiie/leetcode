#!/usr/bin/env python

import unittest
import time

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
提示：使用字典数据格式，会用到循环语句
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

def TwoSum(nums, target):
    """ 
    :nums: 整数数组
    :target: 目标和值
    :returns: 数组中和为目标值的两个数的下标

    """

    d = {}
    no_solution = True
    for index, num in enumerate(nums):
        if not (target - num in d.keys()):
            d[num] = index
        else:
            no_solution = False
            return [d[target-num], index]
    if no_solution:
        print('There is no solution!')
        return [None, None]

class TestTwoSum(unittest.TestCase):

    def test_case1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_result = [0, 1]
        self.assertEqual(TwoSum(nums, target), expected_result)

    def test_case2(self):
        nums = [3, 2, 4]
        target = 6
        expected_result = [1, 2]
        self.assertEqual(TwoSum(nums, target), expected_result)

    def test_case3(self):
        nums = [3, 3, 4]
        target = 6
        expected_result = [0, 1]
        self.assertEqual(TwoSum(nums, target), expected_result)

if __name__ == "__main__":
    unittest.main()
