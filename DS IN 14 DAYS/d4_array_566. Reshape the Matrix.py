class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        old_r = len(mat)
        old_c = len(mat[0])
        if old_r*old_c !=  r*c:
            return mat
        else:
            res = [ [ i for i in range(c) ] for j in range(r) ]
            l = m = 0
            for i in range(r):
                for j in range(c):
                    #print(mat[l][m])
                    #print(res[i][j])
                    res[i][j] = mat[l][m]
                    m += 1
                    if m == old_c:
                        m = 0
                        l += 1
            return res
        