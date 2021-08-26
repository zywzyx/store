

from unittest import TestCase
from demo import  Calc
class TestAddCalc(TestCase):

    def testAdd1(self):
        # 1.造数据
        a = 6
        b = 7
        c = 13

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,sum)

    def testAdd2(self):
        # 1.造数据
        a = 6
        b = -7
        c = -1

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,sum)

    def testAdd3(self):
        # 1.造数据
        a = -6
        b = 7
        c = 1

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,sum)

    def testAdd4(self):
        # 1.造数据
        a = -6
        b = -7
        c = -13

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,sum)


    def testAdd5(self):
        # 1.造数据
        a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        b = 7
        c = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000007

        # 2.开始测试
        calc = Calc()
        sum = calc.add(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,sum)

class TestSubsCalc(TestCase):
    def testSubs1(self):
        #1.造数据
        a = 6
        b = 7
        c = -1

        #2.开始测试
        calc = Calc()
        subs = calc.subs(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,subs)

    def testSubs2(self):
        # 1.造数据
        a = 7
        b = 6
        c = 1

        # 2.开始测试
        calc = Calc()
        subs = calc.subs(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, subs)

    def testSubs3(self):
        # 1.造数据
        a = -6
        b = -7
        c = 1

        # 2.开始测试
        calc = Calc()
        subs = calc.subs(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, subs)

    def testSubs4(self):
        # 1.造数据
        a = 6
        b = -7
        c = 13

        # 2.开始测试
        calc = Calc()
        subs = calc.subs(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, subs)

    def testSubs5(self):
        # 1.造数据
        a = 100000000000000000000000000000000006
        b = 6
        c = 100000000000000000000000000000000000

        # 2.开始测试
        calc = Calc()
        subs = calc.subs(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, subs)

class TestMultiCalc(TestCase):
    def testMulti1(self):
        #1.造数据
        a = 6
        b = 7
        c = 42

        #2.开始测试
        calc = Calc()
        multi = calc.multi(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,multi)

    def testMulti2(self):
        # 1.造数据
        a = 7
        b = 0
        c = 0

        # 2.开始测试
        calc = Calc()
        multi = calc.multi(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)

    def testMulti3(self):
        # 1.造数据
        a = -6
        b = -7
        c = 42

        # 2.开始测试
        calc = Calc()
        multi = calc.multi(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)

    def testMulti4(self):
        # 1.造数据
        a = 6
        b = -7
        c = -42

        # 2.开始测试
        calc = Calc()
        multi = calc.multi(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)

    def testMulti5(self):
        # 1.造数据
        a = 10000000000000000000000000000000000
        b = 6
        c = 60000000000000000000000000000000000

        # 2.开始测试
        calc = Calc()
        multi = calc.multi(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)

class TestDevisionCalc(TestCase):
    def testDevision1(self):
        #1.造数据
        a = 6
        b = 2
        c = 3

        #2.开始测试
        calc = Calc()
        multi = calc.devision(a,b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c,multi)

    def testDevision2(self):
        # 1.造数据
        a = 0
        b = 7
        c = 0

        # 2.开始测试
        calc = Calc()
        multi = calc.devision(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)

    def testMDevision3(self):
        # 1.造数据
        a = -6
        b = 2
        c = -3

        # 2.开始测试
        calc = Calc()
        multi = calc.devision(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)

    def testDevision4(self):
        # 1.造数据
        a = -6
        b = -2
        c = 3

        # 2.开始测试
        calc = Calc()
        multi = calc.devision(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)

    def testDevision5(self):
        # 1.造数据
        a = 10000000000000
        b = 2
        c = 5000000000000

        # 2.开始测试
        calc = Calc()
        multi = calc.devision(a, b)

        # 3.将实际结果与期望结果进行比对
        self.assertEqual(c, multi)
