#昨天作业的讲解
#1.while循环
# while <表达式>
#     循环体
# 2.python基础类型

# 3.字符串处理
# 切片
# 字符串拼接
# 字符串相关函数
# 列表:可变类型
# list1 = [1,2.2,'abc',[4,5,5,'ABC']]
# print(list1[1])
# print(list1[3])
# print(list1[3][1])
# 1>输出列表中第一个元素后所有内容
# print(list1[1:4])
# 2>实现列表的拼接
# list2 = [6,'hhh',6.6]
# print(list1+list2)
# 3>输出列表下表为奇数的元素
# print(list1[1::2])

#python 元组
# python标准类型
#python算数运算符
#函数的定义
#函数的传参:默认参数、指定参数
#练习:封装函数,参数是一个整数,表示打印等腰三角形的层数
#问题:宽度问题,输入时的类型转换
# def isoscelesTriangle(n):
#     maxWidth = 2 * n -1
#     for i in range(1,n+1):
#         starsNum = 2 * i -1
#         star = '*' * starsNum
#         print(star.center(maxWidth))
#
# isoscelesTriangle(5)
# python 局部变量和全局变量
#包的导入
#文件读写

#作业 将三角形打印到1.txt文件中
# def isoscelesTriangle(n):
#     maxWidth = 2 * n -1             #最大宽度
#     for i in range(1,n+1):
#         star = '*' * 2 * i -1       #每行输出
#         print(star.center(maxWidth))


rows = int(input("请等输入腰三角形行数："))             #等腰三角形行数
with open("../Text/1.txt", "w") as file:                    #打开文件,没有则新建
    for i in range(1, rows + 1):
        file.write(" " * (rows - i + 1) + "*" * (2 * i - 1) + "\n")