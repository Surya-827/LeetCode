class Solution:
	def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

		dy = (coordinates[1][1]-coordinates[0][1])
		dx = (coordinates[1][0]-coordinates[0][0])

		for i in range(1,len(coordinates)-1):

			next_dy = (coordinates[i+1][1]-coordinates[i][1])
			next_dx = (coordinates[i+1][0]-coordinates[i][0])

			if dy * next_dx != dx * next_dy:
				return False

		return True