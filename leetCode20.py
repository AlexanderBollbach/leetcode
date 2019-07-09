class Solution(object):
    def isValid(self, s):
        list = []
        for c in s:
            if (len(list) > 0):
                prev = list[-1]  
                if c == ')' and prev == '(' or c == ']' and prev == '[' or c == '}' and prev == '{':
                    list.pop()
                    continue
            list.append(c)
        return len(list) == 0
