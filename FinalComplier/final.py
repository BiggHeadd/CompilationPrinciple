# coding:utf-8
from LexicalAnalysis import LexicalAnalysis
from pathlib import Path

class FinalComplier(LexicalAnalysis):
    def __init__(self):
        super(FinalComplier, self).__init__()
        self.pointer = -1
        self.word = None
        self.tmp_index = 0
        self.middle_code = []
        self.middle_code_index = 0
        self.gotos = []
        self.in_while = 0

    def get_new_tmp(self):
        tmp = "T" + str(self.tmp_index)
        self.tmp_index += 1
        return tmp

    def check_error(self):
        for item in self.result:
            if item[0] == -1:
                return (True, item[2])
        return (False, 0)

    def compile(self, file):
        self.analysis(filename=file)
        # print(self.result)
        invalid, line_index = self.check_error()
        if invalid:
            print("在第 "+str(line_index)+" 行存在不合法的符号")
            return
        self.start()

    def scan(self):
        if self.pointer == len(self.result) - 1:
            self.word = self.result[self.pointer]
            # print(self.word)
        else:
            self.pointer += 1
            self.word = self.result[self.pointer]
            # print(self.word)

    def next_val(self):
        if self.pointer == len(self.result) - 1:
            return (-1, 'end', -1)
        else:
            return self.result[self.pointer + 1]

    def start(self):
        self.scan()
        # 匹配 main
        if not self.word[1] == 'main':
            print("在第 ", self.word[2], " 行缺少'main'")
        else:
            # 匹配 (
            self.scan()
            if not self.word[1] == '(':
                print("在第 ", self.word[2], " 行缺少左括号'('")
            else:
                # 匹配 )
                self.scan()
                if not self.word[1] == ')':
                    print("在第 ", self.word[2], " 行缺少右括号')'")
                else:
                    self.block()

    def block(self):
        # print("enter block")
        self.scan()
        if not self.word[1] == '{':
            print("在第 ", self.word[2], " 行缺少{")
        else:
            self.statement()
            # print("out statement: ", self.word)
            while self.word[1] == ';' or self.word[0] == 10 or self.next_val()[1] != 'end':
                self.statement()
                # print("block: ", self.word)

            # print("need } word: ", self.word)
            if not self.word[1] == '}':
                print("在第 ", self.word[2], " 行缺少}")
            else:
                # print("leave block")
                # self.scan()
                pass

    def statement(self):
        # 读取下一个字符
        self.scan()
        # print("statement: ", self.word)
        if self.word[0] == 10:  # 10是字母
            # 如果是字母开头, 那么是一条语句
            # 保存变量符号
            letter = self.word[1]
            self.scan()
            if self.word[1] == '=':
                self.scan()
                tmp_or_var = self.expression()
                self.middle_code.append((self.middle_code_index, letter, "=", tmp_or_var))
                self.middle_code_index+=1
            else:
                print("在第 ", self.word[2], " 行赋值表达式错误")
        elif self.word[1] == 'if':
            # 如果开头是if, 那么是条件语句
            self.condition()
        elif self.word[1] == 'while':
            # 如果开头是while, 那么是循环语句
            self.loop()
        elif self.word[1] == '}':
            return
        else:
            raise RuntimeError("在第 ", self.word[2], " 行不合法的语句")

    def loop(self):
        # (判断)
        self.in_while+=1
        self.scan()
        if self.word[1] == '(':
            self.scan()
            # print("循环判断语句: ", self.word)
            if self.word[0] == 10 or self.word[0] == 20:
                left = self.word[1]
                self.scan()
                # print("循环判断语句: ", self.word)
                if self.word[1] == '==':  # 待补充
                    sign = self.word[1]
                    self.scan()
                    if self.word[0] == 10 or self.word[0] == 20:
                        right = self.word[1]
                        self.scan()
                        if self.word[1] == ')':
                            self.middle_code.append((self.middle_code_index, "if", left, sign, right, 'goto',
                                                     str(self.middle_code_index + 2)))
                            self.middle_code_index += 1
                            goto_line = self.middle_code_index
                            self.middle_code.append("goto")
                            self.middle_code_index += 1
                            # print(self.middle_code)
                            before = len(self.middle_code)
                            self.block()
                            # print(self.middle_code)
                            # print(before, after)
                            self.middle_code.append((str(self.middle_code_index), 'goto', str(goto_line-1)))
                            self.middle_code_index += 1
                            after = len(self.middle_code)
                            self.middle_code[goto_line] = (str(goto_line), 'goto', str(goto_line + after - before+1))
                            self.scan()
                            self.scan()
                            # print("block out: ", self.word)
                            # print("block_out: ", self.word)
                            # if not self.word[1] == '}':
                            #     print("判断语句错误")
                        else:
                            print("在第 ", self.word[2], " 行循环语句错误")
                    else:
                        print("在第 ", self.word[2], " 行循环语句错误")
                else:
                    print("在第 ", self.word[2], " 行循环语句错误")
            else:
                print("在第 ", self.word[2], " 行循环语句错误")
        else:
            print("在第 ", self.word[2], " 行缺少(")

    def condition(self):
        # (判断)
        self.scan()
        if self.word[1] == '(':
            self.scan()
            # print("判断语句: ", self.word)
            if self.word[0] == 10 or self.word[0] == 20:
                left = self.word[1]
                self.scan()
                # print("判断语句: ", self.word)
                if self.word[1] == '==':  # 待补充
                    sign = self.word[1]
                    self.scan()
                    if self.word[0] == 10 or self.word[0] == 20:
                        right = self.word[1]
                        self.scan()
                        if self.word[1] == ')':
                            before = len(self.middle_code)
                            self.middle_code.append((self.middle_code_index, "if", left, sign, right, 'goto',
                                                     str(self.middle_code_index + 2)))
                            self.middle_code_index += 1
                            goto_line = self.middle_code_index
                            self.middle_code.append("goto")
                            self.middle_code_index += 1
                            before = len(self.middle_code)
                            self.block()
                            after = len(self.middle_code)
                            self.middle_code[goto_line] = (str(goto_line), 'goto', str(goto_line + after - before + 1 + self.in_while))
                            # self.scan()
                            # print("block_out: ", self.word)
                            # if not self.word[1] == '}':
                            #     print("判断语句错误")
                        else:
                            print("在第 ", self.word[2], " 行判断语句错误")
                    else:
                        print("在第 ", self.word[2], " 行判断语句错误")
                else:
                    print("在第 ", self.word[2], " 行判断语句错误")
            else:
                print("在第 ", self.word[2], " 行判断语句错误")
        else:
            print("在第 ", self.word[2], " 行缺少(")

    def expression(self):
        tmp_or_var = self.mat_div()
        while self.word[1] == '+' or self.word[1] == '-':
            sign = self.word[1]
            self.scan()
            tmp_or_var2 = self.mat_div()
            TMP = self.get_new_tmp()
            self.middle_code.append((self.middle_code_index, TMP, "=", tmp_or_var, sign, tmp_or_var2))
            self.middle_code_index += 1
            tmp_or_var = TMP
        return tmp_or_var

    def mat_div(self):
        tmp_or_var = self.factor()
        while self.word[1] == '*' or self.word[1] == '/':
            sign = self.word[1]
            self.scan()
            tmp_or_var2 = self.factor()
            TMP = self.get_new_tmp()
            self.middle_code.append((self.middle_code_index, TMP, "=", tmp_or_var, sign, tmp_or_var2))
            self.middle_code_index += 1
            tmp_or_var = TMP
        return tmp_or_var

    def factor(self):
        # print("factor: ", self.word)
        fplace = None
        if self.word[0] == 10 or self.word[0] == 20:
            fplace = self.word[1]
            self.scan()
        elif self.word[1] == '(':
            self.scan()
            fplace = self.expression()
            if self.word[1] == ')':
                self.scan()
            else:
                print("在第 ", self.word[2], " 行表达式错误")
        else:
            print("在第 ", self.word[2], " 行表达式错误")
        return fplace

    def print_middle_code(self):
        for item in self.middle_code:
            item = [str(i) for i in item]
            # print(item)
            print("(", item[0], ") ", " ".join(item[1:]))


if __name__ == "__main__":
    ### 测试文件路径
    test_filename = "c_LexicalError.txt"

    file_folder = Path("./data_test")
    grammerAnalysis = FinalComplier()
    grammerAnalysis.compile(file_folder / test_filename)
    grammerAnalysis.print_middle_code()