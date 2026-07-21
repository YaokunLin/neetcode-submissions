class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber != 0:
            offset = (columnNumber - 1) % 26
            letter = chr(ord("A") + offset)
            res += letter
            columnNumber = (columnNumber - 1) // 26
        return res[::-1]
        