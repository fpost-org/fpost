import unittest

import TestCore
import TestClasse

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(TestCore)
suite.addTests(loader.loadTestsFromModule(TestClasse))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)