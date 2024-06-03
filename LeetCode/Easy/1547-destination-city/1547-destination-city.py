class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        stack = []
        recent_city = ""
        visited = [0] * len(paths)

        cnt = 100
        while(min(visited) == 0):
            if cnt == 0:
                break
            cnt -= 1
            for i in range(len(paths)):
                if visited[i] == 1:
                    continue
                if len(stack) > 0 or recent_city:
                    if recent_city:
                        if recent_city != paths[i][0]:
                            continue
                    else:
                        recent_city = stack.pop()
                        if recent_city != paths[i][0]:
                            continue

                recent_city = ""
                stack.append(paths[i][1])
                visited[i] = 1
            
        if len(stack) == 0:
            return recent_city
        else:
            return stack[0]