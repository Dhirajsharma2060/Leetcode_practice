class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #reflection
        # hum is liye kar rahe hai kiyu ki first and last la positio bhi swap karna hai 

        for i in range(n):
            #liyu ki pura swap nahi karna hai isliye n//2 ok now consider that 8 rows hai we have to swap on each so kitna swap hoga 
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]        


        
        