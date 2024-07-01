class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = [""]
        shortest_string = strs[0] 
        for string in strs[1:]:
            if len(string) < len(shortest_string):
                shortest_string = string

        stop = False
        i=0
        while i!=len(shortest_string):
            current = strs[0][i]
            for word in strs:
                if word[i] != current:
                    stop = True
                    return "".join(prefix)
                    break
            if stop:
                break
            prefix.append(current)
            i+=1
        return "".join(prefix)
