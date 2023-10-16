class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev_row = [1, 1]
            for i in range(2, rowIndex + 1):
                current_row = [1]
                for j in range(1, len(prev_row)):
                    current_row.append(prev_row[j - 1] + prev_row[j])
                current_row.append(1)
                prev_row = current_row
            return current_row