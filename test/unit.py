import unittest
import Test_DB_Class

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(Test_DB_Class)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)