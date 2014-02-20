#finding a pallindrome

def pallindrome_identifier(n):
    s = str(n)
    s_length= len(s)
    for i in range(s_length/2):
        if s[i] != s[s_length - 1 - i]:
            return False
    return True
   


print pallindrome_identifier(10001)
