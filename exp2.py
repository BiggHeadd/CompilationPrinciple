# coding:utf-8
from exp1 import Compile


class RecursiveDescentAnalysis(Compile):
    def __init__(self):
        super(RecursiveDescentAnalysis, self).__init__()
        self.index = 0
        self.mistake = False
        # self.word = None

    def yuju(self):
        self.statement()
        while self.word[0] == 26:   # ;
            self.scanner()
            if self.word[1] == 'end':
                return
            self.statement()

    def statement(self):
        if self.word[0] == 10:  # letter
            self.scanner()
            if self.word[0] == 18:    # 赋值符号
                self.scanner()
                # print(self.word)
                self.expression()
            elif self.word[1] == 'end':
                return
            else:
                #error
                self.mistake = True
                print("在第 ", self.word[2], " 赋值符号错误")

        else:
            # error
            self.mistake = True
            print("在第 ", self.word[2], " 语句错误")

    def expression(self):
        self.term()
        while self.word[0] == 13 or self.word == 14:    # + -
            self.scanner()
            self.term()

    def term(self):
        self.factor()
        while self.word[0] == 15 or self.word[0] == 16:     # * /
            self.scanner()
            self.factor()

    def factor(self):
        if self.word[0] == 10 or self.word[0] == 11:    # letter or digit
            self.scanner()
        elif self.word[0] == 27:    # (
            self.scanner()
            self.expression()
            if self.word[0] == 28:
                self.scanner()
            else:
                self.mistake = True
                print("在第 ", self.word[2],  " 行缺少 ）")
        else:
            self.mistake = True
            print("在第 ", self.word[2],  "表达式错误")


    def scanner(self):
        self.word = self.result[self.index]
        self.index += 1
        # print(self.word)

    def Recursive(self, file):
        self.complie(file)
        self.scanner()
        if self.word[0] == 1:   # begin
            self.scanner()
            self.yuju()
            if self.word[1] == 'end':
                if self.index == len(self.result) and not self.mistake:
                    print("success")
            else:
                if not self.mistake:
                    print("在第 ", self.word[2], " 行缺少 end")

        else:
            print("在第 ", self.word[2], " 行 begin 错误")
            exit()

if __name__ == "__main__":
    ### 测试文件路径
    test_filename = "./data_test/test_4.txt"
    recursiveDescentAnalysis = RecursiveDescentAnalysis()
    recursiveDescentAnalysis.Recursive(file=test_filename)
