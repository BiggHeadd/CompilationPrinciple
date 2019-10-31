# coding:utf-8

class Compile(object):

    def __init__(self):
        self.keyWordMap = {'begin': 1, 'if': 2, 'then': 3,
                      'while': 4, 'do': 5, 'end': 6,
                      'letter': 10, 'digit': 11, '+': 13,
                      '-': 14, '*': 15, '/': 16,
                      ':': 17, ':=': 18, '<': 20,
                      '<>': 21, '<=': 22, '>': 23,
                      '>=': 24, '=': 25, ';': 26,
                      '(': 27, ')': 28, '#': 0}

        self.calcs = ['+', '-', '*', '/', ':', ':=', '<', '<>', '>', '>=', '=', '<=']
        self.delimiters = [';', '(', ')']
        self.result = []

    def read_data(self, filename):
        with open(filename, 'r', encoding='utf-8')as f:
            return f.read().splitlines()

    def complie(self, filename):
        data = self.read_data(filename=filename)

        for line in data:
            word = ""
            digit = ""
            calc = ""
            line_strip = line.replace("\t", "").replace("\n", "")
            line_p = 0
            len_line = len(list(line_strip))
            zhushi = False
            while line_p < len_line:
                if zhushi:
                    break
                if line_strip[line_p].isalpha():
                    # 开头是字母
                    word += line_strip[line_p]
                    line_p_clone = line_p
                    key = False
                    while line_p_clone+1 < len_line:
                        if line_strip[line_p_clone+1] == '#':
                            zhushi = True
                            break

                        if word in self.keyWordMap.keys():
                            self.result.append((self.keyWordMap[word], word))
                            word = ""
                            key = True
                            break
                        if line_strip[line_p_clone+1].isdigit() or line_strip[line_p_clone+1].isalpha():
                            word += line_strip[line_p_clone+1]
                            line_p_clone+=1
                        else:
                            break
                    line_p = line_p_clone
                    if not key:
                        self.result.append((self.keyWordMap['letter'], word))
                        word = ""
                elif line_strip[line_p].isdigit():
                    # 开头是数字
                    while line_p < len_line:
                        if line_strip[line_p].isdigit():
                            digit+=line_strip[line_p]
                        else:
                            break
                        line_p+=1
                    self.result.append((self.keyWordMap['digit'], digit))
                    digit = ""
                    line_p-=1
                elif line_strip[line_p] in self.calcs:
                    # 开头是运算符
                    if line_strip[line_p] == ':':
                        if line_p+1 < len_line and line_strip[line_p+1]=='=':
                            self.result.append((self.keyWordMap[':='], ':='))
                            line_p+=1
                        else:
                            self.result.append((self.keyWordMap[':'], ':'))
                    elif line_strip[line_p] == '<':
                        if line_p+1 < len_line and line_strip[line_p+1]=='=':
                            self.result.append((self.keyWordMap['<='], '<='))
                            line_p += 1
                        elif line_strip[line_p+1]=='>':
                            self.result.append((self.keyWordMap['<>'], '<>'))
                            line_p += 1
                        else:
                            self.result.append((self.keyWordMap['<'], '<'))
                    elif line_strip[line_p] == '>':
                        if line_p+1 < len_line and line_strip[line_p+1]=='=':
                            self.result.append((self.keyWordMap['>='], '>='))
                            line_p += 1
                        else:
                            self.result.append((self.keyWordMap['>'], '>'))
                    else:
                        self.result.append((self.keyWordMap[line_strip[line_p]], line_strip[line_p]))
                elif line_strip[line_p] in self.delimiters:
                    # 开头是分隔符
                    self.result.append((self.keyWordMap[line_strip[line_p]], line_strip[line_p]))
                elif line_strip[line_p] == '#':
                    break
                line_p += 1

    def print_result(self):
        for each in self.result:
            print(each)



if __name__ == "__main__":
    compile = Compile()
    compile.complie(filename="./data/test.txt")
    compile.print_result()
