#python 类
'''class student:
    def __init__(self,studentID,idCard,name,age):
        self.studentID = studentID          #学号
        self.idCard = idCard                #身份证号
        self.name = name                    #姓名
        self.age = age                      #年龄
    def show(self):
        print("学号:{0}\n姓名:{1}\n姓名:{2}\n年龄{3}".format(self.studentID,self.idCard,self.name,self.age))
    def changeAge(self,age):
        self.age = age
person = student(1234,123456,"张麻子",33)
person.show()
person.changeAge(66)
print("修改后:")
person.show()'''
#numpy基础操作
import numpy as np      #别名

#numpy切片
#numpy 一维数组
# 二维数组

#opencv
"""import cv2
import numpy as np
#加载一张图片
Img = cv2.imread('1.jpg')
print(Img,type(Img))

#显示一张图片
cv2.imshow('src',Img)
#等待按键被按下
key = cv2.waitKey(0)
if 32 == key:
    cv2.imwrite('save.jpg',Img)
cv2.destroyAllWindows()"""



#作业
# 1.更改图片的大小显示更改成200*200
import cv2
img = cv2.imread("Img/1.jpg")
print("原始图像大小:",img.shape,sep="")
cv2.imshow('src',img)
cv2.waitKey(1000)
reshapedImg = cv2.resize(img,(200,200))         #更改图像大小
print("更改后图像大小:",reshapedImg.shape,sep="")
# 2.对图片打马赛克
x, y, w, h = 45, 75, 160-45, 150-75             #处理图像区域
mosaicImg = reshapedImg
pixelArea = mosaicImg[y:y+h, x:x+w]             #坐标系不同
zippedArea = cv2.resize(pixelArea, (10, 10))    #压缩区域
DistortedArea = cv2.resize(zippedArea, (w, h))  #非可逆性还原后的失真图像
mosaicImg[y:y+h, x:x+w] = DistortedArea         #叠加
cv2.imshow('src',mosaicImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

