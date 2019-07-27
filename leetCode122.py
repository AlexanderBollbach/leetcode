def maxProfit(prices):
	if len(prices) == 0 or len(prices) == 1:
		return 0
	
	min = prices[0]
	total = 0
	
	for e1, e2 in zip(prices[:-1], prices[1:]):
		if e2 < e1:
			total += e1 - min
			min = e2

	if prices[-1] - min > 0:
		total += prices[-1] - min

	return total

class Solution(object):
    def maxProfit(self, prices):
        return maxProfit(prices)
        
