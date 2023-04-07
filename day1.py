# 注释:
# 单行注释:#
# '''多行注释
# 多行注释'''
# """多行注释
# 多行注释"""
# 1.输出
# print("Hello World")
#多个输出,默认sep=' ',end = '\n'
# a = 666
# print("a=",a,"六六六")
# print("a=",a,"六六六",sep='*',end='*/\n')
#2.格式化输出
# print("格式化字符串" % （变量1,变量2）)

# print('My name is {0}, My age is {1}'.format(name,age))
# print('My name is {name}, My age is {age}'.format(name='xiaoming',age=12))

# f-string是字符串前面加上 "f"，{}直接使用变量、表达式等。
# print(f'My name is {name},My age is {age}')
# print(f'{name.upper()}')

# 位宽,对齐方式,字符默认左对齐,数字默认右对齐
# print("{:10}".format('*'))
# print("{:<10}".format('*'))     #左对齐
# print("{:>10}".format('*'))     #右对齐
# print("{:^10}".format('*'))     #居中对齐
#
# print("{:10}".format('10'))
# print("{:<10}".format('10'))     #左对齐
# print("{:>10}".format('10'))     #右对齐
# print("{:^10}".format('10'))     #居中对齐

#练习使用print打印一个菱形
# widthMax = 5
#
# for i in range(1,5):
#     k = 0
#     while k< (2*i-1)%5:
#         print("{:^5}".format('*'))
#         k+=1

#文件读写
#变量赋值
#普通赋值   a=1
#多变量赋值 a,b = 1,2
#分支语句
#判断随机数 随机生成0或1,猜硬币
# import random
# coin = random.randint(0,1)
# guess = input()
# if guess==1:
#     if coin ==1:
#         print("YES")
#     else:
#         print("NO")
# else:
#     if coin == 1:
#         print("NO")
#     else:
#         print("YES")
#循环语句
#99乘法表
# for i in range(1,10):
#     for j in range(1,i):
#         print(j,"×",i,"=",i*j,sep='',end=' ')
#     print("")

#作业:猜拳 0,1,2代表剪刀石头布
# print("规则:0代表剪刀,1代表石头,2代表布")
# fingerGuess = input("剪刀石头布:")
import random

print("0代表剪刀，1代表石头，2代表布。")

while True:
    # 让玩家出拳
    player = input("请输入你的选项（0/1/2）：")

    # 验证玩家输入的选项是否合法
    if player not in ['0', '1', '2']:
        print("无效的选项，请重新输入。")
        continue

    # 将玩家输入的选项转换成整数
    player = int(player)

    # 让电脑出拳
    computer = random.randint(0, 2)

    # 打印玩家和电脑出拳的结果
    print("你出了 %d，电脑出了 %d。" % (player, computer))

    # 判断胜负
    if player == computer:
        print("平局！")
    elif player == 0 and computer == 1:
        print("你输了！")
    elif player == 1 and computer == 2:
        print("你输了！")
    elif player == 2 and computer == 0:
        print("你输了！")
    else:
        print("你赢了！")

    # 是否继续游戏
    choice = input("是否继续游戏？（Y/N）：")
    if choice != 'Y' and choice != 'y':
        break

print("游戏结束，谢谢参与！")
