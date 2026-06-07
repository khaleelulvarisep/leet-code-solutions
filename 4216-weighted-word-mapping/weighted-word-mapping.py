class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alph=a[::-1]
        result=''
        for w in words:
            sum=0
            for s in w:
                sum+=weights[a.index(s)]
            result+=alph[sum%26]
        return result    


        


        





        