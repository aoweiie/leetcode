#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import time

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        else:
            a, b = 0, x
            while a + 1 != b:
                middle = int((a + b) / 2)
                if middle ** 2 <= x:
                    a = middle
                else:
                    b = middle
            return a

class TestSqrt(unittest.TestCase):

    def test_case1(self):
        x = 0
        expected_result = 0
        solution = Solution()
        self.assertEqual(solution.mySqrt(x), expected_result)

    def test_case2(self):
        x = 1
        expected_result = 1
        solution = Solution()
        self.assertEqual(solution.mySqrt(x), expected_result)

    def test_case3(self):
        x = 8
        expected_result = 2
        solution = Solution()
        self.assertEqual(solution.mySqrt(x), expected_result)

    def test_case4(self):
        x = 1000
        expected_result = 31
        solution = Solution()
        self.assertEqual(solution.mySqrt(x), expected_result)

        
if __name__ == "__main__":
    unittest.main()
