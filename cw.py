from tkinter import *


class Demo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('CROSSWORD_DEMO')
        self.pack(fill=BOTH, expand=0)
        self.sqsize = 50
        for row in range(10):
            for col in range(10):
                top = row * self.sqsize + 2
                left = col * self.sqsize + 2
                bottom = row * self.sqsize + self.sqsize
                right = col * self.sqsize + self.sqsize
                cas.create_rectangle(left, top, right, bottom, outline='white', fill='black')
        cas.pack()
        # Các từ và cách đặt các từ
        self.a = ('math', 'physic', 'music', 'literature', 'history')
        self.style = ("ngang", "doc", "doc", "doc", "ngang")
        self.rowWords = (5, 4, 5, 0, 1)
        self.colWords = (2, 5, 7, 3, 2)

        # create number and word
        def generateHang(rowPosition, colPosition, lenghtOfWord, wordOrder):
            for col in range(colPosition, lenghtOfWord + colPosition):
                top = rowPosition * self.sqsize + 2
                left = col * self.sqsize + 2
                bottom = rowPosition * self.sqsize + self.sqsize
                right = col * self.sqsize + self.sqsize
                cas.create_rectangle(left, top, right, bottom, fill='white')
            cas.create_text(colPosition * self.sqsize + 10, rowPosition * self.sqsize + 10, text=wordOrder + '.',
                            font=('Times', 10))

        def generateCot(rowPosition, colPosition, lenghtOfWord, wordOrder):
            for row in range(rowPosition, lenghtOfWord + rowPosition):
                top = row * self.sqsize + 2
                left = colPosition * self.sqsize + 2
                bottom = row * self.sqsize + self.sqsize
                right = colPosition * self.sqsize + self.sqsize
                cas.create_rectangle(left, top, right, bottom, fill='white')
            cas.create_text(colPosition * self.sqsize + 10, rowPosition * self.sqsize + 10, text=wordOrder + '.',
                            font=('Times', 10))

        for word in range(0, len(self.a)):
            if self.style[word] == "doc":
                # colPo = int(input("chon cot:"))
                # rowPo = int(input("chon hang:"))
                colPo = self.colWords[word]
                rowPo = self.rowWords[word]
                generateCot(rowPo, colPo, len(self.a[word]), str(word + 1))
            if self.style[word] == "ngang":
                # colPo = int(input("chon cot:"))
                # rowPo = int(input("chon hang:"))
                colPo = self.colWords[word]
                rowPo = self.rowWords[word]
                generateHang(rowPo, colPo, len(self.a[word]), str(word + 1))

        """
        #hang
        for col in range(4, len(self.a[0]) + 4):
            row = 2
            top = row * self.sqsize + 2
            left = col * self.sqsize + 2
            bottom = row * self.sqsize + self.sqsize
            right = col * self.sqsize + self.sqsize
            cas.create_rectangle(left, top, right, bottom, fill='white')
            cas.create_text(4 * self.sqsize + 10, 2* self.sqsize + 10, text="1.", font=('Times', 10))
            
        for col in range(1, len(self.a[2]) + 1):
            row = 0
            top = row * self.sqsize + 2
            left = col * self.sqsize + 2
            bottom = row * self.sqsize + self.sqsize
            right = col * self.sqsize + self.sqsize
            cas.create_rectangle(left, top, right, bottom, fill='white')
            cas.create_text(1 * self.sqsize + 10, 0 * self.sqsize + 10, text="3.", font=('Times', 10))

        # cot
        for row in range(1, len(self.a[1]) + 1):
            col = 3
            top = row * self.sqsize + 2
            left = col * self.sqsize + 2
            bottom = row * self.sqsize + self.sqsize
            right = col * self.sqsize + self.sqsize
            cas.create_rectangle(left, top, right, bottom, fill='white')
            cas.create_text(3 * self.sqsize + 10, 1 * self.sqsize + 10, text="2.", font=('Times', 10))

        for row in range(0, len(self.a[4]) + 0):
            col = 9
            top = row * self.sqsize + 2
            left = col * self.sqsize + 2
            bottom = row * self.sqsize + self.sqsize
            right = col * self.sqsize + self.sqsize
            cas.create_rectangle(left, top, right, bottom, fill='white')
            # cas.create_text(left + 25, top + 25, text=a[4][wordCount5], font=('Times', 16))
            # wordCount5 = wordCount5 + 1
            cas.create_text(9 * self.sqsize + 10, 0 * self.sqsize + 10, text="5.", font=('Times', 10))

        for row in range(0, len(self.a[3]) + 0):
            col = 6
            top = row * self.sqsize + 2
            left = col * self.sqsize + 2
            bottom = row * self.sqsize + self.sqsize
            right = col * self.sqsize + self.sqsize
            cas.create_rectangle(left, top, right, bottom, fill='white')
            # cas.create_text(left + 25, top + 25, text=a[3][wordCount4], font=('Times', 16))
            # wordCount4 = wordCount4 + 1
            cas.create_text(6 * self.sqsize + 10, 0 * self.sqsize + 10, text="4.", font=('Times', 10))
            """
        # questions of hints
        cas.create_text(600, 10, anchor=W, font="VNI-Dom 18", text='1.' + self.a[0])
        cas.create_text(600, 40, anchor=W, font="VNI-Dom 18", text='2.' + self.a[1])
        cas.create_text(600, 70, anchor=W, font="VNI-Dom 18", text='3.' + self.a[2])
        cas.create_text(600, 100, anchor=W, font="VNI-Dom 18", text='4.' + self.a[3])
        cas.create_text(600, 130, anchor=W, font="VNI-Dom 18", text='5.' + self.a[4])

        # button
        self.button1 = Button(tk, text="win1", command=lambda: self.unhide(1))
        self.button2 = Button(tk, text="win2", command=lambda: self.unhide(2))
        self.button3 = Button(tk, text="win3", command=lambda: self.unhide(3))
        self.button4 = Button(tk, text="win4", command=lambda: self.unhide(4))
        self.button5 = Button(tk, text="win5", command=lambda: self.unhide(5))
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()

    def unhide(self, number):
        wordCount1 = 0
        #wordCount2 = 0
        #wordCount3 = 0
        #wordCount4 = 0
        #wordCount5 = 0
        if self.style[number - 1] == "ngang":
            for col in range(self.colWords[number - 1], len(self.a[number - 1]) + self.colWords[number - 1]):
                row = self.rowWords[number - 1]
                top = row * self.sqsize + 2
                left = col * self.sqsize + 2
                cas.create_text(left + 25, top + 25, text=self.a[number - 1][wordCount1], font=('Times', 16))
                wordCount1 = wordCount1 + 1
        if self.style[number - 1] == "doc":
            for row in range(self.rowWords[number - 1], len(self.a[number - 1]) + self.rowWords[number - 1]):
                col = self.colWords[number - 1]
                top = row * self.sqsize + 2
                left = col * self.sqsize + 2
                cas.create_text(left + 25, top + 25, text=self.a[number - 1][wordCount1], font=('Times', 16))
                wordCount1 = wordCount1 + 1
        """
        if number == 1:
            if self.style[0] == "ngang":
                for col in range(self.colWords[0], len(self.a[0]) + self.colWords[0]):
                    row = self.rowWords[0]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    bottom = row * self.sqsize + self.sqsize
                    right = col * self.sqsize + self.sqsize
                    cas.create_text(left + 25, top + 25, text=self.a[0][wordCount1], font=('Times', 16))
                    wordCount1 = wordCount1 + 1
            if self.style[0] == "doc":
                for row in range(self.rowWords[0], len(self.a[0]) + self.rowWords[0]):
                    col = self.colWords[0]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    bottom = row * self.sqsize + self.sqsize
                    right = col * self.sqsize + self.sqsize
                    cas.create_text(left + 25, top + 25, text=self.a[0][wordCount1], font=('Times', 16))
                    wordCount1 = wordCount1 + 1
        if number == 2:
            if self.style[1] == "ngang":
                for col in range(self.colWords[1], len(self.a[1]) + self.colWords[1]):
                    row = self.rowWords[1]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[1][wordCount2], font=('Times', 16))
                    wordCount1 = wordCount1 + 1
            if self.style[1] == "doc":
                for row in range(self.rowWords[1], len(self.a[1]) + self.rowWords[1]):
                    col = self.colWords[1]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[1][wordCount2], font=('Times', 16))
                    wordCount2 = wordCount2 + 1
        if number == 3:
            if self.style[2] == "ngang":
                for col in range(self.colWords[2], len(self.a[2]) + self.colWords[2]):
                    row = self.rowWords[2]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[2][wordCount3], font=('Times', 16))
                    wordCount3 = wordCount3 + 1
            if self.style[2] == "doc":
                for row in range(self.rowWords[2], len(self.a[2]) + self.rowWords[2]):
                    col = self.colWords[2]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[2][wordCount3], font=('Times', 16))
                    wordCount3 = wordCount3 + 1
        if number == 4:
            if self.style[3] == "ngang":
                for col in range(self.colWords[3], len(self.a[3]) + self.colWords[3]):
                    row = self.rowWords[3]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[3][wordCount4], font=('Times', 16))
                    wordCount4 = wordCount4 + 1
            if self.style[3] == "doc":
                for row in range(self.rowWords[3], len(self.a[3]) + self.rowWords[3]):
                    col = self.colWords[3]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[3][wordCount4], font=('Times', 16))
                    wordCount4 = wordCount4 + 1

        if number == 5:
            if self.style[4] == "ngang":
                for col in range(self.colWords[4], len(self.a[4]) + self.colWords[1]):
                    row = self.rowWords[4]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[4][wordCount5], font=('Times', 16))
                    wordCount5 = wordCount5 + 1
            if self.style[4] == "doc":
                for row in range(self.rowWords[4], len(self.a[4]) + self.rowWords[4]):
                    col = self.colWords[4]
                    top = row * self.sqsize + 2
                    left = col * self.sqsize + 2
                    cas.create_text(left + 25, top + 25, text=self.a[4][wordCount5], font=('Times', 16))
                    wordCount5 = wordCount5 + 1

"""


if __name__ == '__main__':
    tk = Tk()
    cas = Canvas(tk, width=1000, height=500)
    # tk.geometry("420x250+300+300")
    demo = Demo(tk)
    tk.mainloop()
