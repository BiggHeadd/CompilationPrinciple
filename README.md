# 编译原理实验

## 系统环境:
- python3.6
- 没有使用到特别的库, 后续有使用到的时候会添加进来

## 实验一: 词法分析
- 运行方法:
    - 命令行运行: python exp1.py
    - pycharm idea 运行: 选中exp1.py, 选择运行

- 测试数据设置:
    - 默认测试数据在data_test文件夹下面
    - exp1.py 里面的 main 中 设置test_filename
    ```
    if __name__ == "__main__":
    ### 测试文件路径
        test_filename = "./data/test.txt"
    ```

- 符号对应的种别码:

符号|种别|符号|种别|符号|种别
----|----|----|----|----|----
'begin'| 1 | 'if'| 2 | 'then'| 3
'while'| 4 | 'do'| 5 | 'end' | 6,
'letter'| 10| 'digit'| 11| '+'| 13
'-'| 14| '*'| 15| '/'| 16
':'| 17| ':='| 18| '<'| 20
'<>'| 21| '<='| 22| '>'| 23
'>='| 24| '='| 25| ';'| 26
'('| 27| ')'| 28

## 测试结果
- 测试数据一:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp1/test_data_1.png)
![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp1/test_result_1.png)

- 测试数据二:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp1/test_data_2.png)
![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp1/test_result_2.png)


# 实验二: 递归下降语法分析实验
- 运行方法:
    - 命令行运行: python exp2.py
    - pycharm idea 运行: 选中exp2.py, 选择运行
    
- 测试数据设置
    - 测试数据设置:
    - 默认测试数据在data_test文件夹下面
    - exp1.py 里面的 main 中 设置test_filename
    ```
    if __name__ == "__main__":
    ### 测试文件路径
        test_filename = "./data/test.txt"
    ```
 
- 测试数据一:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp2/3.png)

- 测试数据二:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp2/4.png)

- 测试数据三:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp2/5.png)

- 测试数据四:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp2/6.png)

# 实验三: 递归下降语法制导翻译实验
- 运行方法:
    - 命令行运行: python exp3.py
    - pycharm idea 运行: 选中exp3.py, 选择运行
    
- 测试数据设置
    - 测试数据设置:
    - 默认测试数据在data_test文件夹下面
    - exp1.py 里面的 main 中 设置test_filename
    ```
    if __name__ == "__main__":
    ### 测试文件路径
        test_filename = "./data/test.txt"
    ```

- 测试数据一:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp3/1.png)

- 测试数据二:

![Image text](https://github.com/BiggHeadd/CompilationPrinciple/blob/master/pic/exp2/2.png)