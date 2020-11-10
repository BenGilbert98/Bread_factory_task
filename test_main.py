from naan_factory import Factory
import unittest


class naan_factory_test(unittest.TestCase):
    factory = Factory()

    # expected to return "no naan" as there isn't any dough when the test runs
    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_dough(), "no naan")

    # expected to return "dough" as arguments "flour" and "water" are passed
    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough("flour", "water"), "dough")

    # testing to see if order of arguments matters
    def test_make_dough_two(self):
        self.assertEqual(self.factory.make_dough("water", "flour"), "dough")

    # expected to return "dough" as arguments "flour" and "water" are passed
    def test_run_factory(self):
        self.assertEqual(self.factory.run_factory("flour", "water"), "naan")

    # testing to see if order of arguments matters
    def test_run_factory_two(self):
        self.assertEqual(self.factory.run_factory("flour", "water"), "naan")