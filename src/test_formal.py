import pytest
import unittest as ut

from regular_expr_reader import RegularExpressionReader

ERROR_MSG = ["Regular expression has improper symbols", "Incorrect expression"]

class TestClassRegularExpressionReader:
    def test_initiation_1(self):
        with pytest.raises(AttributeError) as e:
            A = RegularExpressionReader("ad.b+*")
        assert e.value.args[0] == ERROR_MSG[0]

    
    def test_initiation_2(self):
        with pytest.raises(AttributeError) as e:
            A = RegularExpressionReader("ac.a+*a")
        assert e.value.args[0] == ERROR_MSG[1]
        

    def test_sum_1(self):
        expr1 = [1, 0, 3]
        expr2 = [-1, 2, 1]
        my_func = RegularExpressionReader._RegularExpressionReader__ExprSum 
        res = my_func(expr1, expr2)
        assert res == [1, 0, 1]
        

    def test_sum_2(self):
        expr1 = [-1, 0, -1, -1, -1]
        expr2 = [1, 0, 1, 0, 1]
        my_func = RegularExpressionReader._RegularExpressionReader__ExprSum 
        res = my_func(expr1, expr2)
        assert res == expr2


    def test_concat_1(self):
        expr1 = [0, 0, 0]
        expr2 = [-1, 0, -1]
        my_func = RegularExpressionReader._RegularExpressionReader__ExprConcatenation
        res = my_func(expr1, expr2)
        assert res == [1, 0, 0]


    def test_concat_2(self):
        expr1 = [4, 7, 3, -1, 1]
        expr2 = [3, -1, 2, 1, 5]
        my_func = RegularExpressionReader._RegularExpressionReader__ExprConcatenation
        res = my_func(expr1, expr2)
        assert res == [5, 4, 3, 5, 4]      

    
    def test_clini_star_1(self):
        expr = [-1, 0, 3, 2]
        my_func = RegularExpressionReader._RegularExpressionReader__ExprRepeated
        res = my_func(expr)
        assert res == [0, 0, 0, 0]

    
    def test_clini_star_2(self):
        expr = [2, 1]
        my_func = RegularExpressionReader._RegularExpressionReader__ExprRepeated
        res = my_func(expr)
        assert res == [0, 1]


    def test_clini_star_3(self):     
        expr = [-1, 0, -1]
        my_func = RegularExpressionReader._RegularExpressionReader__ExprRepeated
        res = my_func(expr)
        assert res == [0, 0, 0]


    def test_FindMinLenEqualToRemainderByMod_1(self):
        A = RegularExpressionReader("acb..bab.c.*.ab.ba.+.+*a.")
        assert A.FindMinLenEqualToRemainderByMod(3, 0) == None


    def test_FindMinLenEqualToRemainderByMod_2(self):
        A = RegularExpressionReader("ab+c.aba.*.bac.+.+*")
        assert A.FindMinLenEqualToRemainderByMod(3, 1) == 4
