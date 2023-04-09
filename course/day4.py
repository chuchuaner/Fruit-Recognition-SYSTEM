"""mport numpy as np
import cv2
# 1.彩色图片转灰度图片
srcImg = cv2.imread('1.jpg')
gray_img = cv2.cvtColor(srcImg,cv2.COLOR_BGR2GRAY)
cv2.imshow('src',gray_img)
key = cv2.waitKey(2000)
# 2.保存灰度图片
cv2.imwrite('grag.jpg',gray_img)
cv2.waitKey()
cv2.destroyAllWindows()
# 3.打开摄像头
cam = cv2.VideoCapture(0)
cam.isOpened()                  #判断是否打开
while True:
    ret,frame = cam.read()      #视频中取一帧图像,返回值是否成功
    if not ret:
        break
    #图像上写文本
    cv2.putText(frame,'zsl',(200,400),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)
    cv2.rectangle(frame,())
    cv2.imshow('video',frame)   #显示图像
    ret = cv2.waitKey(30)
    #a按下ESC退出
    if ret == 27
        cv2.destroyAllWindows()
        break
#释放摄像头
cam.release()"""
import cv2

"""# 4.人眼的检测
from cv2 import *
#人眼检测模型路径,轻量级模型
path = "E:/Python/Anaconda/envs/anaconda_3-7/Library/etc/haarcascades/haarcascade_eye.xml"
cam = VideoCapture(0)
while True:
    ret,frame = cam.read()
    if not ret:
        continue
    # 将人眼识别模型添加到级联分类器
    casede = CascadeClassifier(path)
    #图像转灰度
    gray = cvtColor(frame,COLOR_BGR2GRAY)
    #用分类器进行分类得到人眼出现的起始坐标宽高
    eye = casede.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(16,16))
    #进行数据处理
    for rect in eye:
        x,y,w,h = rect
        rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        #显示图像
        imshow('video',frame)
    if waitKey(10) == 27:
        break
cam.release()"""
#人脸检测模型路径,轻量级模型
"""from cv2 import *
path = "E:/Python/Anaconda/envs/anaconda_3-7/Library/etc/haarcascades/haarcascade_frontalface_alt2.xml"
cam = VideoCapture(0)
while True:
    ret,frame = cam.read()
    if not ret:
        continue
    # 将人眼识别模型添加到级联分类器
    casede = CascadeClassifier(path)
    #图像转灰度
    gray = cvtColor(frame,COLOR_BGR2GRAY)
    #用分类器进行分类得到人眼出现的起始坐标宽高
    face = casede.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))
    #进行数据处理
    for rect in face:
        x,y,w,h = rect
        rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        #显示图像
        imshow('video',frame)
    if waitKey(10) == 27:
        break
cam.release()"""
"""#KNN
from sklearn.datasets import load_iris                  #莺尾花数据集
from sklearn.neighbors import KNeighborsClassifier      #KNN
from sklearn.model_selection import train_test_split    #分离训练集合测试集
def load_datasets():
    iris = load_iris()
    data = iris.data
    label = iris.target
    x,x1,y,y1 = train_test_split(data,label,test_size=0.2)
    return x,x1,y,y1
# 加载数据集
x_train,x_test,y_train,y_test = load_datasets()
#创建KNN模型
knn = KNeighborsClassifier(n_neighbors=15)
#将数据集带入模型
knn.fit(x_train,y_train)
# 验证模型
y_pre = knn.predict(x_test)
print("y_pre:",y_pre)
print("y_test",)"""

# 作业:使用KNN进行手写数字识别
from sklearn.datasets import load_digits                #加载数据集
from sklearn.neighbors import KNeighborsClassifier      #KNN
from sklearn.model_selection import train_test_split    #分离训练集合测试集
def load_datasets():
    iris = load_digits()
    data = iris.data
    label = iris.target
    x,x1,y,y1 = train_test_split(data,label,test_size=0.2)
    return x,x1,y,y1
x_train,x_test,y_train,y_test = load_datasets() # 加载数据集
knn = KNeighborsClassifier(n_neighbors=15)      #创建KNN模型
knn.fit(x_train,y_train)                        #将数据集带入模型
#加载图像,灰度方式
"""img = cv2.imread('',0)
img = cv2.resize(img,(8,8))
img = img.reshape(1,-1)"""
y_pre = knn.predict(x_test)                     # 验证模型
print("y_pre:",y_pre)
print("y_test",y_test)
len = y_pre.size
print("测试集长度:",y_pre.size,sep="")
rightNum = 0
for i,j in list(zip(y_pre,y_test)):
    if i == j:
        rightNum += 1
print("正确率:{:.2%}".format(rightNum/len))

