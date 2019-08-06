runcount = 0
memocount = 0

def run(s, words, memo):
	global memocount
	global runcount
	for word in words:
		# print('word in s', word, s, memo)
		runcount += 1
		if s.find(word, 0) == 0:
			newStr = s.replace(word, '', 1)

			if newStr != '' and newStr not in memo:
				run(newStr, words, memo)
			
			if newStr == '':
				memo[s] = True
			elif newStr in memo:
				# print('hit memo')
				# print(memo)
				memocount += 1
				memo[s] = memo[newStr]
			
			
				

class Solution(object):
    def wordBreak(self, s, wordDict):
		memo = {}
		run(s, wordDict, memo)
		print(memo)
		print('runcount', runcount)
		print('memocount', memocount)
		return s in memo and memo[s]

a = ("leetcode", ["leet", "code"])
b = ('ababa', ["aba", "ba"])
c = ('ababababababababba', ["abba", "aba","bab"])
d = ("catsandog", ["cats","dog","sand","and","cat"])
e = ("123456dead", ["1", "2", "12","3", "123", "23", "4","34","234","1234","5","45","345","234","2345","6","56","2345","23456", '12345', "dead"])
f = ("aaaaa", ["a"])
g = ("acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb", ["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"])
h = ('abba', ["ab", "a"])
i = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
r = Solution().wordBreak(*i)
print(r)


