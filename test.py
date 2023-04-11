import  os
"""import torch

# 测试CUDA是否可用
train_on_gpu = torch.cuda.is_available()

if not train_on_gpu:
        print('CUDA is not available. Training on CPU')
else:
        print('CUDA is available. Training on GPU')

# 选择GPU
device = torch.device("cuda:0" if train_on_gpu else "cpu")"""

# 配置神经网络、该函数为自定义函数
# model_test = model_unet(model_Inputs[0], 3, 1)

# 将网络在gpu中运行
# model_test.to(device)
# 在代码中调用命令行
a = os.system(
        f"python ./yolov5-7.0/detect.py --weights ./Model/Fruits.pt --img 640 --source 0")
# import tensorflow as tf
# print(tf.test.is_gpu_available())
# import tensorflow as tf
# print(tf.test.is_gpu_available())
import torch
print(torch.cuda.is_available())