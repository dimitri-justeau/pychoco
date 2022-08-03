import unittest

from pychoco import create_model


class TestMin(unittest.TestCase):

    def testMin(self):
        m = create_model()
        a = m.intvar(0, 5)
        b = m.intvars(5, 0, 5)
        m.min(a, *b).post()
        sols = m.get_solver().find_all_solutions()
        for s in sols:
            vals = [s.get_int_val(i) for i in b]
            self.assertEqual(min(vals), s.get_int_val(a))
