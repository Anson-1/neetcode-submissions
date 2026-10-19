class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + '#' + i
        return s 

    def decode(self, s: str) -> List[str]:
        words = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != '#':
                j += 1
            word_len = int(s[index:j])
            begin = j+1
            end = begin+word_len
            word = s[begin:end]
            words.append(word)
            index = end
        return words

        
