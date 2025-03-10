class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        def get_adjacent_points(sr, sc, org):
            adjacent = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            adjacent_points = [(sr + ad[0], sc+ad[1]) for ad in adjacent if 0<=sr+ ad[0]< m and 0<=sc+ad[1] < n and image[sr+ad[0]][sc+ad[1]] == org]
            return adjacent_points

        org = image[sr][sc]
        start = (sr, sc)
        m, n = len(image), len(image[0])
        image[sr][sc] = color
        visited = set((sr, sc))
        adjacent_points = get_adjacent_points(sr, sc, org)

        while( adjacent_points):
            last = adjacent_points[0]
            visited.add(last)
            image[last[0]][last[1]] = color
            ad_points = get_adjacent_points(last[0], last[1], org)
            filtered = []
            for  ad in ad_points:
                if ad not in visited:
                    filtered.append(ad)

            adjacent_points = adjacent_points[1:] + filtered

        return image

