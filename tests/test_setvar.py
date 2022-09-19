import unittest

from pychoco import create_model


class TestSetVar(unittest.TestCase):

    def test_create_setvar(self):
        model = create_model("MyModel")
        lb = set([0, 1, 2])
        ub = set([0, 1, 2, 3, 4])
        s = model.setvar(lb, ub)
        llb = s.get_lb()
        uub = s.get_ub()
        self.assertEqual(lb, llb)
        self.assertEqual(ub, uub)
        ss = model.setvar(lb, name="ss")
        self.assertEqual(ss.name, "ss")
        self.assertEqual(ss.get_value(), lb)
