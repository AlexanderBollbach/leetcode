qs =  [
    # ("abcatsanddog", ["a", "b", "ab", "cat", "cats", "and", "sand", "dog"]),
    # ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),
    # ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
]

run_count = 0

def run(s, words, memo):
    if s in memo:
        print('hit memo')
        return memo[s]
    global run_count
    sents = []
    print(s)
    for i in range(len(s)):
        run_count += 1
        ss = s[0:i + 1]
        if ss in words:
            rest = s[i + 1: len(s)]
            if rest == '':
                sents.append(ss)
            r = run(rest, words, memo)
            sents += map(lambda x: ss + " " + x, r)

    memo[s] = sents
    return sents

class Solution(object):
    def wordBreak(self, s, wordDict):
        return run(s, wordDict, {})


print('===')
for q in qs:
    r = Solution().wordBreak(q[0], q[1])
    print(run_count)
    print(r)

        