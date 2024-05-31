class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        result = 0
        unconnect = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += 1
                    cnt = 0
                    for k in range(len(grid)):
                        if grid[k][j] == 1:
                            cnt += 1

                    if cnt > 1:
                        continue

                    cnt = 0
                    for k in range(len(grid[0])):
                        if grid[i][k] == 1:
                            cnt += 1

                    if cnt > 1:
                        continue

                    unconnect += 1


        result -= unconnect
        return result