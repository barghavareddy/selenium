import unittest
class Pay_ment(unittest.TestCase):
    def test_payment_dollers(self):
        print("payment in dollers")
        self.assertTrue(True)
    def test__payment__rupees(self):
        print("payment in rupees")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()