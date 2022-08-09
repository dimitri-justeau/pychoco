import unittest

from pychoco import create_model


class TestLexLess(unittest.TestCase):

    def testLexLess1(self):
        m = create_model()
        ar1 = m.intvars(3, 0, 5)
        ar2 = m.intvars(3, -1, 4)
        c = m.lex_less(ar1, ar2)
        c.post()
        while m.get_solver().solve():
            self.assertTrue(c.is_satisfied())
        self.assertTrue(m.get_solver().get_solution_count() > 0)
