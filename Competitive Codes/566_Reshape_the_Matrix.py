from typing import List

class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        :param mat:
        :param r:
        :param c:
        :return:
        """

        if(len(mat)**2!=r*c):return mat
        flat_mat ,prop_mat= [], []

        for i in range(len(mat)):
            for j in range(mat[i]):
                flat_mat.append(j)
        edge = c
        for i in range(len(flat_mat),edge):
            prop_mat.append(flat_mat[i:edge])
            edge+=c
        return prop_mat
