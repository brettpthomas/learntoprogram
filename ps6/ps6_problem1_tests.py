from ps6 import RectangularRoom

import unittest

class TestNumTilesOf5x8Room(unittest.TestCase): 
	def runTest(self): 

		# create a room with width=5 and height=8
		room = RectangularRoom(5, 8)

		# make sure its num tiles is 40
		self.assertEqual(room.getNumTiles(), 40)

if __name__ == "__main__": 
	unittest.main()
	