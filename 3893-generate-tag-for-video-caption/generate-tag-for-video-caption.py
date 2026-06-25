class Solution:
    def generateTag(self, caption: str) -> str:
        
        cap=caption.strip()
        result='#'
        
        if cap:

            result+=cap[0].lower()
 
        flag=False
        for i in range(1,len(cap)):

            if cap[i]==' ':
                flag=True
                continue
            if flag:
                result+=cap[i].upper()  
                flag=False
            else:
                result+=cap[i].lower()    

        if len(result)>100:
            return result[:100]
        else:
            return result    





           


           
              

            
            
        