# https://leetcode.com/problems/word-search/description/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(idx_i: int, idx_j: int, path: str):

            if path == word or path[::-1] == word:
                result = True
                return result
            if idx_i >= len(board) or idx_j >= len(board[0]):
                return

            for i in range(idx_i, len(board)):
                for j in range(idx_j, len(board)):
                    result1 = backtrack(i+1, j, path+board[i][j])
                    if result1:
                        return True
                    result2 = backtrack(i, j+1, path+board[i][j])
                    if result2:
                        return True
                    # if board[i][j] != word:
                    #     continue
        result = False
        result = backtrack(0, 0, "")
        return result


sol = Solution()

assert sol.exist(board=[["A", "B"], ["C", "S"]], word="ABS") == True

assert sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                 "A", "D", "E", "E"]], word="ABCCED") == True
assert sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                 "A", "D", "E", "E"]], word="SEE") == True
assert sol.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                 "A", "D", "E", "E"]], word="ABCB") == False
