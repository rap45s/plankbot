# -*- coding: utf-8 -*-

import unittest

from app
from test
import sys

if __name__ == "__main__":
    lock = unittest.TestLoader().loadTestsFromTestCase(TestLock)
    suite = unittest.TestSuite([lock])
    unittest.TextTestRunner(verbosity=2).run(suite)
