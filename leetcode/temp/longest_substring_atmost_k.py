# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def longest_substring(s,k):
    char_map=dict()
    max_str=[None, None]
    max_len=0
    st=0
    en=0
    distinct=0
    while en< len(s):
        if not char_map.get(s[en],False):
            char_map[s[en]]=True
            distinct+=1
            if distinct>k:
                char_map[s[st]]= False
                st+=1
                distinct-=1
        if en-st+1 > max_len:
            max_len=en-st+1
            max_str=[st,en]
        en+=1
    return s[max_str[0]:max_str[1]+1]

print longest_substring("abcba",2)
