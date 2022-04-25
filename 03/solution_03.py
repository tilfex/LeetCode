class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        res = 0
        chars = [None] * 128 #creating a list for all possible characters
        
        while i < len(s):
            x = s[i] #current character
            pos = chars[ord(x)] #getting the previous position in the list of the current character
            
            if pos != None and pos >= j and pos < i: #if the character is already in the current substring
                j = pos + 1 #change starting position of substring to +1 of the previous character position
            
            res = max(res, i - j +1) #getting the max length of res or i-j+1 (position of current substring)
            
            chars[ord(x)] = i #puts the current position of the current character into the list
            i += 1 #add 1 to i for next step of loop
        return res #return the result after finishing the loop