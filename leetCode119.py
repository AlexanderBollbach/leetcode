class Solution(object):
	def getRow(self, rowIndex):
		count = 0

		lastRow = [1]
		
		while True:
			if count == rowIndex:
				return lastRow

			nextRow = []
			
			for e1, e2 in zip(lastRow[:-1], lastRow[1:]):
				nextRow.append(e1 + e2)
			
			lastRow = ([1] + nextRow + [1])

			count += 1
