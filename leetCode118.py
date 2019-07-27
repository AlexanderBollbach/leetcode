class Solution(object):
	def generate(self, numRows):

		if numRows == 0:
			return []
			
		rows = [[1]]
		
		while True:
			if len(rows) == numRows:
				return rows
			nextRow = []
			for e1, e2 in zip(rows[-1][:-1], rows[-1][1:]):
				nextRow.append(e1 + e2)
			rows.append([1] + nextRow + [1])
