class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        # create a dict of nodes with next nodes
        nodes = dict()
        for r in range(rows):
            for c in range(cols):
                # next nodes
                nextNodes = []
                if c+1 < cols and matrix[r][c] < matrix[r][c+1]:
                  nextNodes.append( (r,c+1) )
                if -1 < c-1 and matrix[r][c] < matrix[r][c-1]:
                  nextNodes.append( (r,c-1) )
                if r+1 < rows and matrix[r][c] < matrix[r+1][c]:
                  nextNodes.append( (r+1,c) )
                if -1 < r-1 and matrix[r][c] < matrix[r-1][c]:
                  nextNodes.append( (r-1,c) )
                
                # prev nodes
                prevNodes = []
                if c+1 < cols and matrix[r][c] > matrix[r][c+1]:
                  prevNodes.append( (r,c+1) )
                if -1 < c-1 and matrix[r][c] > matrix[r][c-1]:
                  prevNodes.append( (r,c-1) )
                if r+1 < rows and matrix[r][c] > matrix[r+1][c]:
                  prevNodes.append( (r+1,c) )
                if -1 < r-1 and matrix[r][c] > matrix[r-1][c]:
                  prevNodes.append( (r-1,c) )

                nodes[(r,c)] = [prevNodes,nextNodes]

        Nonly = set()

        for nodeKey, nodeValue in nodes.items():
            if len(nodeValue[0]) == 0:
                Nonly.add(nodeKey)
        
        NorLess = Nonly

        # start wave loop
        n, more = 0, True
        while more:
            n += 1
            NplusOne = set( next for node in Nonly for next in nodes[node][1] )
            if len(NplusOne) == 0: break
            Nonly = set(node for node in NplusOne if set(nodes[node][0]).issubset(NorLess))
            NorLess = NorLess | Nonly

        return n        