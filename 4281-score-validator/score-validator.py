class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        result=[]
        for c in events:
            if counter==10:
                break
            if c=="W":
                counter+=1
            elif c=="WD":
                score+=1
            elif c=="NB":
                score+=1
            else:
                score+=int(c)
        result.append(score)
        result.append(counter) 
        return result       
                


        