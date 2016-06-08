import unittest
import os
from sliding_window import slidingw

class ManageTest(unittest.TestCase):
	def test_generateIntersectPatches_Always_Positive(self):
		s = slidingw(640.0,480.0)
		result = s.generateIntersectingPatches(1,1,100)
		self.assertEqual(all(x[0] >=0 for x in result),True)
		self.assertEqual(all(x[1] >=0 for x in result),True)		
	def test_generateIntersectPatches_produces_requested_count(self):
		s = slidingw(640.0,480.0)
		result = s.generateIntersectingPatches(1,1,10)
		self.assertEqual(len(result), 10)
		result = s.generateIntersectingPatches(1,1,1)
		self.assertEqual(len(result), 1)
		result = s.generateIntersectingPatches(1,1,100)
		self.assertEqual(len(result), 100)
		result = s.generateIntersectingPatches(1,1,1000)
		self.assertEqual(len(result), 1000)
		
if __name__ == '__main__':
    unittest.main()
