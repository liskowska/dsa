"""
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
"""

def longestPalindrome_brute(s):
    longest_lenght = 0
    longest_word = None
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > longest_lenght:
                    longest_lenght = len(s[i:j])
                    longest_word = s[i:j]
    return longest_word

def longestPalindrome_dp(s):
    n = len(s)
    longest_lenght = 0
    longest_word = None
    word = ""

    for i in range(n):
        # palindromy nieparzyste
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            word = s[l:r+1]
            if word == s[l:r+1][::-1] and len(word) > longest_lenght:
                longest_word = word
                longest_lenght = len(word)
            l -= 1
            r += 1

        # palindromy parzyste
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            word = s[l:r+1]
            if word == s[l:r+1][::-1] and len(word) > longest_lenght:
                longest_word = word
                longest_lenght = len(word)
            l -= 1
            r += 1
    return longest_word


s1 = "babad" # bab, aba
s2 = "cbbd" # bb

print(longestPalindrome_brute(s1))
print(longestPalindrome_brute(s2))

print(longestPalindrome_dp(s1))
print(longestPalindrome_dp(s2))
