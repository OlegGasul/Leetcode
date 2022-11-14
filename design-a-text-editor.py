class TextEditor:

    def __init__(self):
        self.s = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.s = self.s[ : self.cursor] + text + self.s[self.cursor : ]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        new_cursor = max(0, self.cursor - k)
        noOfChars = k if self.cursor - k >= 0 else self.cursor
        self.s = self.s[ : new_cursor] + self.s[self.cursor : ]
        self.cursor = new_cursor
        return noOfChars

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        start = max(0, self.cursor - 10)
        return self.s[start : self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.s), self.cursor + k)
        start = max(0, self.cursor - 10)
        return self.s[start : self.cursor]

textEditor = TextEditor()
print(textEditor.addText("leetcode"))   # The current text is "leetcode|".
print(textEditor.deleteText(4))         # return 4
                                        # The current text is "leet|". 
                                        # 4 characters were deleted.
print(textEditor.addText("practice"))   # The current text is "leetpractice|". 
print(textEditor.cursorRight(3))        # return "etpractice"
                                        # The current text is "leetpractice|". 
                                        # The cursor cannot be moved beyond the actual text and thus did not move.
                                        # "etpractice" is the last 10 characters to the left of the cursor.
print(textEditor.cursorLeft(8))         # return "leet"
                                        # The current text is "leet|practice".
                                        # "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
print(textEditor.deleteText(10))        # return 4
                                        # The current text is "|practice".
                                        # Only 4 characters were deleted.
print(textEditor.cursorLeft(2))         # return ""
                                        # The current text is "|practice".
                                        # The cursor cannot be moved beyond the actual text and thus did not move. 
                                        # "" is the last min(10, 0) = 0 characters to the left of the cursor.
print(textEditor.cursorRight(6))        # return "practi"
                                        # The current text is "practi|ce".
                                        # "practi" is the last min(10, 6) = 6 characters to the left of the cursor.