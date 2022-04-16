class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        #print(m, n)
        
        minn = 0
        maxx = m*n - 1
        
        while maxx >= minn:
            mid = minn + (maxx - minn) // 2
            r = mid // n
            c = mid % n
            
            if matrix[r][c] == target:
                return True 
            elif matrix[r][c] > target:
                maxx = mid - 1
            elif matrix[r][c] < target:
                minn = mid + 1
        return False