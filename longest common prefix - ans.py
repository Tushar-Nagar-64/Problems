class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        s1 = ""
        
        if not strs:
            return ""
        
        else:
            
            if len(strs)==1:
                return strs[0]
            
            else:
                
                strs.sort()
                for x,y in zip(strs[0],strs[-1]):
                    if x==y: s1+=x
                        
                    else: 
                        break
            

            
        return s1


    
