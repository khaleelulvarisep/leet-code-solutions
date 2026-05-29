class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        c=[]
        for i in range(len(matrix)):
            c.append(sum(matrix[i]))

        
        return c    

    

        