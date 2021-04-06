class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not len(strs):
            return ""
        
        prefix = strs[0]
        
        for s in strs:
            newprefix = ""
            len_prefix = len(prefix)
            
            for j in range(0,min(len_prefix,len(s))): 
               
                if prefix[j] == s[j]:
                    newprefix = f'{newprefix}{prefix[j]}'
                else:
                    break
            prefix = newprefix
            
        return prefix
            