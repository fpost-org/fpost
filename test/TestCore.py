import unittest

class TestUM(unittest.TestCase):

    def testAssertTrue(self):
        self.assertTrue(True)

    def testFailUnless(self):
        self.assertTrue(True)

    def testFailIf(self):
        self.assertFalse(False)

    def testAssertFalse(self):
        self.assertFalse(False)

    def testEqual(self):
        self.assertEqual(1, 3 - 2)

    def testNotEqual(self):
        self.assertNotEqual(2, 3 - 2)

    def testEqualFail(self):
        self.assertNotEqual(1, 2)

    def testNotEqualFail(self):
        self.assertEqual(2, 3 - 1)

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3 - 2.0, places=0)

if __name__ == '__main__':
    unittest.main()