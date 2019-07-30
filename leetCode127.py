def isEditDistanceOne(l, r):
	return len(list(filter(lambda x: x[0] != x[1], zip(l, r)))) <= 1

def ladder(b, e, words, chain):

	print('=======')
	print('b e', b, e)
	print(words)
	print(chain)

	if b == e:
		# print('end')
		# print(chain)
		return chain

	if len(words) == 0:
		return None

	vals = []

	for w in words:

		nextWord = None
		
		if b in words:
			nextWord = b
		elif e in words and isEditDistanceOne(e, b):
			nextWord = e
		elif isEditDistanceOne(w, b):
			nextWord = w
			if len(chain) == 0:
				chain = [b]

		print('next word ', nextWord)

		if nextWord:
			print(chain)
			f = list(filter(lambda x: x != nextWord, words))
			for idx, val in enumerate(chain):
				if isEditDistanceOne(nextWord, val):
					chain = chain[0:idx + 1] + [nextWord]
					break
			if not chain:
				chain = [nextWord]
			val = ladder(nextWord, e, f, chain)
			if val != None:
				return val
				# vals.append(val)



	# print('vals ---')
	# print(vals)

	# final = min(vals) if vals else None

	# print('return final ', final)

	# return final
	# return None

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        val = ladder(beginWord, endWord, wordList, [])
        return len(val) if val else 0


# a = 'dog'
# b = 'lag'
# c = ['lag', 'fig', 'dal', 'fol','fag', 'dig', 'dog']

# a = "teach"
# b = "place"
# c = ["peale","wilts","place","fetch","purer","pooch","peace","poach","berra","teach","rheum","peach"]

# a = "hit"
# b = "cog"
# c = ["hot","dot","dog","lot","log","cog"]

# a = "hot"
# b = "dog"
# c = ["hot","cog","dog","tot","hog","hop","pot","dot"]

# a = "qa"
# b = "sq"
# c = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

a = "cat"
b = "fin"
c = ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]

r = Solution().ladderLength(a,b,c)
print(r)


