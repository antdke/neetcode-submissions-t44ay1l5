class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # create 3 list of sets
            # list of 9 sets - rows
            # list of 9 sets - columns
            # 2D list of 3 lists each with 3 sets - for the subgrids

        # traverse board (2D array)

        # check if current element in each list of set, is so return False

        # if not, then add element to each list of set

        # continue

        # if no element returns False, return True

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        subgrids = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                # early continue
                if num == ".":
                    continue

                if num in rows[r]:
                    return False

                if num in columns[c]:
                    return False

                if num in subgrids[r // 3][c // 3]:
                    return False

                rows[r].add(num)
                columns[c].add(num)
                subgrids[r // 3][c // 3].add(num)
        
        return True