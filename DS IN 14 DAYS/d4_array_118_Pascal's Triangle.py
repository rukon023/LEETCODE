class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for r in range(1, numRows+1):
            row = []
            for i in range(r):
                #print(r, i)
                if i == 0:
                    row.append(1)
                elif i == r-1:
                    row.append(1)
                else:
                    row.append(ans[r-2][i-1] + ans[r-2][i])

            ans.append(row)
            #print(ans)
        return ans