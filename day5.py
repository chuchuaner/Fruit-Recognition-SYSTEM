#手动导入数据训练
"""import cv2
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from os import listdir

#获取数据
data = []       #存储训练数据
label = []      #存储训练标签
#读取亩,分会文件名的列表
namelist = listdir('trainingDigits')
#遍历所有文件
for filename in namelist:
    file = []
    #读取文件内容
    with open('trainingDigits/'+filename,'r') as fd:
        #删除换行符,字符串转数字
        ret = fd.readlines()
        for i in ret:
            for j in range(32):     #每行索引32个元素为换行符不要
                file.append(int(i[j]))
        data.append(file)
    #获取对应标签
    label.append(filename[0])
#将蓄念数据和训练标签转化为numpy数组
data = np.array(data)
label = np.array(label)
#创建KNN模型
KNN = KNeighborsClassifier(n_neighbors=17)
#将数据带入模型
KNN.fit(data,label)
#加载图像,灰度方式
img = cv2.imread('./img/8.jpg',0)
img = cv2.resize(img,(32,32))
img = img.reshape(1,-1)
y_pre = KNN.predict(img)
print(y_pre)"""
#线性回归
#深度学习和神经网络
#梯度下降
#激活函数
#卷积神经网络CNN
"""import cv2
import numpy as np
from keras.layers import *
from sklearn.datasets import load_digits
from sklearn.model_selection import  train_test_split
from keras.utils import to_categorical
from keras import Sequential
#加载数据
def load_data():
    x_train,x_test,y_train,y_test = train_test_split(load_digits().data,load_digits().target,test_size=0.2)
    x_train = x_train.reshape(len(x_train[:,0]),8,8,1)
    x_test = x_test.reshape(x_test.shape[0],8,8,1)
    # 热编码
    y_train = to_categorical(y_train,num_classes=10, dtype=int)
    return x_train,x_test,y_train,y_test
x_train,x_test,y_train,y_test = load_data()
#创建神经网络模型
def creat_model():
    # 1.创建神经网络对象
    model = Sequential()
    # 2.搭建神经网络
    # 2.1搭建卷积层
    model.add(Conv2D(filters=8,kernel_size=(2,2),input_shape=(8,8,1),activation='relu'))
    # 2.2创建池化层
    model.add(MaxPool2D((2,2)))
    #2.3丢去数据
    model.add(Dropout(rate=0.2))
    # 2.4一维化处理
    model.add(Flatten())
    #3创建全连接层
    # 3.1输入层 input_dim:输入的维度,特征个数   units:神经元的个数
    model.add(Dense(input_dim=8*8*1,units=32,activation='relu'))
    # 3.2输出层
    model.add(Dense(units=10,activation='softmax'))     #数值随机
    #模型配置
    model.compile(optimizer='adam',loss='mse')
    print("神经网络搭建完成")
    return model
model = creat_model()
#4.训练:训练数据,训练标签,训练一次大小,论述,显示模式
model.fit(x_train,y_train,batch_size=10,epochs=100,verbose=1)
print("训练完成")
#保存模型
model.save('./Model/cnn_num.h5')
print("模型已经保存")

#5.预测
y_pre = model.predict(x_test)
y_pre = np.argmax(y_pre,axis=1)
#6.计算准确率
y_test1 = to_categorical(y_test,num_classes=10,dtype=int)
loss = model.evaluate(x_test,y_test1)
print('最终损失值',loss)
print('真实值:',y_test)
print('预测值',y_pre)
#计算错误个数
n = 0
for i in range(len(y_pre)):
    if y_pre[i] != y_test[i]:
        n +=1
print('总数:',len(y_pre))
print('错误个数:',n)

#图片预测
pic = cv2.imread('./Img/8.jpg',0)
pic = cv2.resize(pic, dsize=(8,8))
pic = pic.reshape((1,8,8,1))
ret = model.predict(pic)
print(np.argmax(ret,axis=1))"""
#作业编写代码尝试应用训练出的模型进行CNN数字识别
import numpy as np
import cv2
from keras.models import load_model
model = load_model('./Model/cnn_num.h5')
#图片预测
pic = cv2.imread('./Img/8.jpg',0)
pic = cv2.resize(pic, dsize=(8,8))
pic = pic.reshape((1,8,8,1))
ret = model.predict(pic)
print(np.argmax(ret,axis=1))