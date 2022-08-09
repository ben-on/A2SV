class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stk=[(sr,sc)]
        visited=set()
        goal=image[sr][sc]
        while stk:
            temp=stk.pop()
            visited.add(temp)
            image[temp[0]][temp[1]]=color
            ways=[(temp[0],temp[1]+1),(temp[0]+1,temp[1]),(temp[0],temp[1]-1),(temp[0]-1,temp[1])]
            for pair in ways:
                if pair[0] in range(len(image)) and pair[1] in range(len(image[0])):
                    if image[pair[0]][pair[1]]==goal and pair not in visited:
                        stk.append(pair)
        return image
                        