class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for w in words:
            valid=True
            for c in w:
                if c not in allowed:
                    valid=False
                    break  
            if valid:
                count+=1    
                    
        return count            

        
        