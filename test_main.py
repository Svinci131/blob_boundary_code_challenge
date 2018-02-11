import unittest
from blob import Blob 

class TestBorderBoundaryFinder(unittest.TestCase):
	def test_basic(self):
		test_input = [
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,1,1,1,0,0,0,0,0],
			[0,0,1,1,1,1,1,0,0,0],
			[0,0,1,0,0,0,1,0,0,0],
			[0,0,1,1,1,1,1,0,0,0],
			[0,0,0,0,1,0,1,0,0,0],
			[0,0,0,0,1,0,1,0,0,0],
			[0,0,0,0,1,1,1,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
		]

		test_output = Blob(test_input)
		self.assertEqual(test_output.boundaries['Top'], 1)
		self.assertEqual(test_output.boundaries['Left'], 2)
		self.assertEqual(test_output.boundaries['Bottom'], 7)
		self.assertEqual(test_output.boundaries['Right'], 6)
		self.assertEqual(test_output.boundaries['Cell_Reads'], 44)

	def test_left_further_than_top(self):
		test_input = [
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
			[0,0,1,1,1,1,1,0,0,0],
			[0,0,1,0,0,0,1,0,0,0],
			[0,0,1,1,1,1,1,0,0,0],
			[0,0,0,0,1,0,1,0,0,0],
			[0,0,0,0,1,0,1,0,0,0],
			[0,0,0,0,1,1,1,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
		]

		test_output = Blob(test_input)
		self.assertEqual(test_output.boundaries['Top'], 1)
		self.assertEqual(test_output.boundaries['Left'], 2)
		self.assertEqual(test_output.boundaries['Bottom'], 7)
		self.assertEqual(test_output.boundaries['Right'], 6)
	
	def test_right_spaced(self):
		test_input = [
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,1,0,0,0,0,1,0,0],
			[0,0,1,1,1,1,1,1,0,0],
			[0,0,1,0,0,0,1,0,0,0],
			[0,0,1,1,1,1,1,1,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
		]

		test_output = Blob(test_input)
		self.assertEqual(test_output.boundaries['Top'], 1)
		self.assertEqual(test_output.boundaries['Left'], 2)
		self.assertEqual(test_output.boundaries['Bottom'], 4)
		self.assertEqual(test_output.boundaries['Right'], 7)

	def test_whole_grid_blob(self):
		test_input = [
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1,1,1,1],
		]

		test_output = Blob(test_input)
		self.assertEqual(test_output.boundaries['Top'], 0)
		self.assertEqual(test_output.boundaries['Left'], 0)
		self.assertEqual(test_output.boundaries['Bottom'], 9)
		self.assertEqual(test_output.boundaries['Right'], 9)
		self.assertEqual(test_output.boundaries['Cell_Reads'], 100)

	def test_small_blob(self):
		test_input = [
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,1],
		]

		test_output = Blob(test_input)
		self.assertEqual(test_output.boundaries['Top'], 9)
		self.assertEqual(test_output.boundaries['Left'], 9)
		self.assertEqual(test_output.boundaries['Bottom'], 9)
		self.assertEqual(test_output.boundaries['Right'], 9)
		#self.assertEqual(test_output.boundaries['Cell_Reads'], 0) 

	def test_no_blob(self):
		test_input = [
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
		]

		try:
			test_output = Blob(test_input)
		except BaseException as e:
			self.assertEqual(str(e), 'Grid does not contain blob')

if __name__ == '__main__':
    unittest.main()