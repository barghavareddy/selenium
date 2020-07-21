import unittest
from package2.paymenttest import Pay_ment
from package2.returns import Returns
from package_1.logintest import Login_test
from package_1.signuptest import Sign_up
t1=unittest.TestLoader().loadTestsFromTestCase(Pay_ment)
t2=unittest.TestLoader().loadTestsFromTestCase(Returns)
t3=unittest.TestLoader().loadTestsFromTestCase(Login_test)
t4=unittest.TestLoader().loadTestsFromTestCase(Sign_up)
#craetion tests suites
sanitytests=unittest.TestSuite([t3,t4])
mastertests=unittest.TestSuite([t3,t4,t1,t2])
functionaltests=unittest.TestSuite([t1,t2])



#unittest.TextTestRunner(verbosity=2).run(sanitytests)
#unittest.TextTestRunner(verbosity=2).run(functionaltests)
unittest.TextTestRunner(verbosity=2).run(mastertests)