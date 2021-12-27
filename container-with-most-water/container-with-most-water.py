class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """        

        if len(height) == 2:
            return min(height)**2

        def area(A, i, j):
            return min(A[i] , A[j]) * (j - i)

        a, z = 0, len(height)-1
        i, j = a, z

        while a < z and i < j:

            if height[i] <= height[j]:
                i = i+1
            else:
                j = j-1

            if area(height, i, j) > area(height, a, z) and i != j :
                a, z = i, j


        return area(height, a, z)
        