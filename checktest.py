#
# Lab 5-2:
#
#   testtime.py: Lab 4.5
#
# Python unit tests for Lab 5-1's
#
# Copy your...
#

''' Unit test case for Lab 4.4's calctime(secs) function '''

import unittest

class TestTime(unittest.TestCase): # inherit from TestCase

    def test_1(self): # test methods MUST start with 'test'
        self.assertEqual((0,0,0,0,0),compare(0))

    def test_2(self): # test method
        self.assertEqual((0,0,0,1,0),compare(0))

  # add more of your own tests

      # look at Python doc for other assert methods...

# if we try to run this as module, execute the main of unittest

if __name__ == '__main__':
    unittest.main(exit=False) # the default param needs this setup:
                              # Thanks, StackOverflow.com!
