import unittest
class Sign_up(unittest.TestCase):
    def test_sign__gmail(self):
        print("signup gmail-----")
        self.assertTrue(True)

    def test_signupfacebook(self):
        print("signup facebook-----")
        self.assertTrue(True)

    def test_signupgmail(self):
        print("sign up twitter-----")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()