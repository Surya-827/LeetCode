
# WAY 1
def strip_string(s):
    i = 0
    while i < len(s) and s[i].isspace():
        i = i + 1
    j = len(s) - 1
    while j >= 0 and s[j].isspace():
        j = j - 1
    striped_string = s[i:j + 1]

    return striped_string

#WAY 2
def split_string(s):
    words = []
    word = ""

    for char in s:
        if char != " ":
            word += char
        else:
            words.append(word)
            word = ""
    words.append(word)

    return words

#WAY 3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = split_string(strip_string(s))
        last_word = words[-1]
        return len(last_word)