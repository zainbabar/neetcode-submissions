class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # only digs 1-9 no dups for row and col and box
        # when we see a dig in a row or col add it to a hash table
        # make sure we havent seen this before so hash table val is none?

        # 2 lists of hashtables, all hashtables are empty for now
        row_tables = [{} for _ in range(len(board))]
        col_tables = [{} for _ in range(len(board[0]))]
        box_tables = [{} for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                
                if val == ".":
                    continue

                # we have not seen this number in the current row before
                if row_tables[row].get(val) is None:
                    row_tables[row][val] = True
                # we have seen this num in the current row so theres a dup
                # not valid
                else:
                    print(val)
                    print("failed at row check")
                    return False
                # have not seen this number in the current col before
                if col_tables[col].get(val) is None:
                    col_tables[col][val] = True
                else:
                    print(val)
                    print("failed at col check")
                    return False

                # need to figure out what box we are supposed to be in based on our row/col
                # can get the row of boxes we are by doing row // 3 (0, 1, or 2)
                # and the col of boxes we are in by doing col // 3 (0, 1, or 2)
                # box num is then (row * 3) + col
                box_num = (row // 3) * 3 + (col // 3)

                # havent seen this val yet in current box
                if box_tables[box_num].get(val) is None:
                    box_tables[box_num][val] = True
                else:
                    print(val)
                    print(row, col)
                    print("failed at box check")
                    return False

        return True

    # prev logic covers dups in rows or cols now we need to check the 3x3 boxes
    # first box is rows 0-2 and cols 0-2, 2nd is rows 0-2 and cols 3-5
