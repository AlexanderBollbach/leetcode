def findMin(lists):	
	lists = lists[::-1]
	while len(lists) > 1:
		lower = lists[0]
		upper = lists[1]
		for i in range(len(upper)):
			upper[i] = min(upper[i] + lower[i], upper[i] + lower[i + 1])
		lists = lists[1:]
	return lists[0][0]

class Solution(object):
    def minimumTotal(self, triangle):
    	return findMin(triangle)
