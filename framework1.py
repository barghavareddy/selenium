import unittest


class Advancese(unittest.TestCase):
    # @classmethod
    def setUp(self):
        print("before log")

    # @classmethod
    def tearDown(self):
        print("after log")

    # @unittest.SkipTest
    def test_B(self):
        print("test 1")

    @unittest.skipIf(1 == 1, "pending actions")
    def test_C(self):
        print("test 2")
    @unittest.skip("no--------")
    def test_D(self):
        print("test 3")

    def test_E(self):
        print("test 4")


if __name__ == "__main__":
    unittest.main()
