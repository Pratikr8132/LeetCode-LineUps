class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a=0
        for i in range(len(s)):
            temp=[]
            temp.append(s[i])
            for j in range(i+1,len(s)):
                if s[i]!=s[j] and s[j] not in temp:
                    temp.append(s[j])
                else:
                    break
            
            a=max(len(temp),a)
    
        return a