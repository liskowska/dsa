"""
647. Palindromic substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
"""

def countSubstring_dp(s):
    n = len(s)
    palindrom_cnt = 0

    for i in range(n):
        # palindromy nieparzyste
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            word = s[l:r+1]
            if word == s[l:r+1][::-1]: palindrom_cnt += 1
            l -= 1
            r += 1

        # palindromy parzyste
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            word = s[l:r+1]
            if word == s[l:r+1][::-1]:
                palindrom_cnt += 1
            l -= 1
            r += 1
    return palindrom_cnt

s1 = "babad"
s2 = "cbbd"
s3 = "aaa"

print(countSubstring_dp(s1))
print(countSubstring_dp(s2))
print(countSubstring_dp(s3))