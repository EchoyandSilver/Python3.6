# -*- coding: utf-8 -*-

# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过

import unittest

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if not isinstance(self.score,int):
            raise TypeError('分数必须为整数')
        if self.score >100 or self.score < 0:
            raise ValueError('分数必须在1到100之间')
        if self.score >= 80 and self.score <=100:
            return 'A'
        if self.score >= 60 and self.score < 80:
            return 'B'
        return 'C'

class TestStudent(unittest.TestCase):

# 这两个方法会分别在每调用一个测试方法的前后分别被执行。
#    def setUp(self):
#        print('setUp...')
#
#    def tearDown(self):
#        print('tearDown...')

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()

