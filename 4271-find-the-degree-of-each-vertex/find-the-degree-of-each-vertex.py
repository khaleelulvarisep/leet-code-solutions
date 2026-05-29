class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result=[]
        for i in range(len(matrix)):
            result.append(sum(matrix[i]))
        return result    

    

        