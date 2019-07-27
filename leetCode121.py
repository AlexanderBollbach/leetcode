def maxProfit(prices):
	if len(prices) == 0 or len(prices) == 1:
		return 0
	
	min = prices[0]
	max = 0
	
	for price in prices[1:]:
		if price - min > max:
			max = price - min
		if price < min:
			min = price

	return max

class Solution(object):
    def maxProfit(self, prices):
        return maxProfit(prices)
