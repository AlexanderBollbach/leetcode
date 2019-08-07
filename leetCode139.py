allQs = [
("leetcode", ["leet", "code"], True, 'a'),
('ababab', ["aba", "ba"], False, 'b'),
('ababababaabba', ["aba","bab","abba"], True, 'c'),
("catsandog", ["cats","dog","sand","and","cat"], False, 'd'),
("123456dead", ["1", "2", "12","3", "123", "23", "4","34","234","1234","5","45","345","234","2345","6","56","2345","23456", '12345', "dead"], True, 'e'),
("aaaaa", ["a"], True, 'f'),
("acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb", ["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"], True, 'g'),
("abcd", ["a","abc","b","cd"], True, 'h'),
("cars", ["car","ca","rs"], True, 'i'),
("aaaab", ["a","aa","aaa", "b"], True, 'j'),
("aaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"], True, 'k'),
("abcd", ["a","abc","b","cd"], True, 'l')
]

current = None

runcount = 0
memocount = 0

def run(s, words, memo):

	global runcount
	global memocount

	if s in memo:
		memocount += 1
		return
	
	for word in words:
		runcount += 1
		# print('=== s: {} | word: {} | memo: {}'.format(s, word, memo))
		if s.find(word, 0) == 0:
			s2 = s.replace(word, '', 1)
			run(s2, words, memo)
			# if s2 in memo and memo[s2]:
			if s not in memo or not memo[s]:
				memo[s] = memo[s2]
			# if s not in memo or:
				# print('set memo s', s, s2)
				# memo[s] = memo[s2]

	if s not in memo:
		# print('false memo', s)
		memo[s] = False

class Solution(object):
		def wordBreak(self, s, wordDict):
			memo = {'': True}
			run(s, wordDict, memo)
			# print(memo)
			# print('runcount', runcount)
			# print('memocount', memocount)
			return s in memo and memo[s]


for val in allQs:
	sol = Solution().wordBreak(val[0], val[1])
	print('running test: {} and got {}'.format(val[3], sol))
	if sol != val[2]:
		raise Exception('problem with', val[3])

if current:
	print(Solution().wordBreak(*current))
	


