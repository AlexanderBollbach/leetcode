def without(words, word):
	return list(filter(lambda x: x != word, words))

def dist(l, r):
	return len(list(filter(lambda x: x[0] != x[1], zip(l, r)))) == 1

def ladder(b, e, words, chain):

	if dist(b, e):
		print('chain ', chain + [e])
		return 

	next_links = list(filter(lambda x: dist(x, b), words))
	for link in next_links:
		words = without(words, link)
		ladder(link, e, words, next_links)
	print(next_links)
	

	



		




class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        r = ladder(beginWord, endWord, wordList, [])
        print(r)
        return len(r)
        

# a = 'a'
# b = 'c'
# c = ['a','b','c']

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

a = "qa"
b = "sq"
c = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

# a = "cat"
# b = "fin"
# c = ["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"]

r = Solution().ladderLength(a,b,c)
print(r)


