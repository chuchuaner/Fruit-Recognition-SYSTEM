# 作业讲解
# 讨论水果识别需求,识别到水果后机械臂做什么动作
# 串口配置
import serial
import time
import serial.tools.list_ports
from pynput import keyboard
import numpy as np
import threading

class armControl():
    def __init__(self):
        # 生成一个16*2的二维数组，行数代表引脚编号，第一列表示up次数，第二列表示down次数
        self.controlCount = np.zeros_like(np.arange(0,16))
        self.currentPinOfLead = 4
        self.perAngle = 10
        self.ser = None

    def controlArmsByKeyboard(self):
        t1 = threading.Thread(target=self.listenKeyboard)
        t1.start()

    def setArmPerAngle(self, perAngle):
        self.perAngle = perAngle

    def listenKeyboard(self):
        def listenKey(key):
            print("当前key：", key)
            if hasattr(key,"char") and key.char.isdigit():
                self.currentPinOfLead = int(key.char)
                print("当前引脚已设置为：", self.currentPinOfLead)
            elif key == keyboard.Key.up:
                if self.controlCount[self.currentPinOfLead]*self.perAngle < 180:
                    self.controlCount[self.currentPinOfLead] += 1
                self.setArmAngleByKeyboard()
                print("引脚{}：角度为{}\n\n".format(self.currentPinOfLead,self.controlCount[self.currentPinOfLead]*self.perAngle))
            elif key == keyboard.Key.down:
                if self.controlCount[self.currentPinOfLead] > 0:
                    self.controlCount[self.currentPinOfLead] -= 1
                self.setArmAngleByKeyboard()
                print("引脚{}：角度为{}\n\n".format(self.currentPinOfLead,self.controlCount[self.currentPinOfLead]*self.perAngle))
            elif key == keyboard.Key.tab:
                self.showAllKeyboardInfo()
            elif key == keyboard.Key.esc:
                self.resetArmsAngle()
            elif key == keyboard.Key.cmd:
                self.armGet()
            elif key == keyboard.Key.alt_l:
                self.putFruit(70)
        with keyboard.Listener(on_press=listenKey) as listener:
            listener.join()


    # 机械臂移动到抓取位置
    def armGet(self):
        cmd = [
            bytes.fromhex("ff 02 04 {}".format(self.angleToHex(157))),
            bytes.fromhex("ff 02 05 {}".format(self.angleToHex(122))),
            bytes.fromhex("ff 02 06 {}".format(self.angleToHex(40))),
            bytes.fromhex("ff 02 07 {}".format(self.angleToHex(165))),
            bytes.fromhex("ff 02 08 {}".format(self.angleToHex(0))),
        ]
        for i in range(len(cmd)):
            self.ser.write(cmd[i])
            time.sleep(3.5)

    # 输入水果的种类，放入不同的盘子
    def putFruit(self,angleToP):
        cmd = [
            bytes.fromhex("ff 02 08 {}".format(self.angleToHex(70))),
            bytes.fromhex("ff 02 05 {}".format(self.angleToHex(70))),
            bytes.fromhex("ff 02 04 {}".format(self.angleToHex(angleToP))),
            bytes.fromhex("ff 02 05 {}".format(self.angleToHex(122))),
            bytes.fromhex("ff 02 08 {}".format(self.angleToHex(0))),
        ]
        for i in range(len(cmd)):
            self.ser.write(cmd[i])
            time.sleep(3.5)

    def showAllKeyboardInfo(self):
        for i in range(len(self.controlCount)):
            print("引脚{}：角度为{}".format(i, self.controlCount[i] * self.perAngle))

    def resetArmsAngle(self):
        self.controlCount[4] = 160//self.perAngle
        self.controlCount[5] = 100//self.perAngle
        self.controlCount[6] = 90 // self.perAngle
        self.controlCount[7] = 90 // self.perAngle
        self.controlCount[8] = 0 // self.perAngle
        cmd = [
        "ff 02 04 {}".format(self.angleToHex(self.controlCount[4]*self.perAngle)),
        "ff 02 05 {}".format(self.angleToHex(self.controlCount[5]*self.perAngle)),
        "ff 02 06 {}".format(self.angleToHex(self.controlCount[6]*self.perAngle)),
        "ff 02 07 {}".format(self.angleToHex(self.controlCount[7]*self.perAngle)),
        "ff 02 08 {}".format(self.angleToHex(self.controlCount[8]*self.perAngle)),
            "ff 02 07 {}".format(self.angleToHex(self.controlCount[7] * self.perAngle)),
               ]
        print(cmd)
        for i in range(len(cmd)):
            write_len = self.ser.write(bytes.fromhex(cmd[i]))
            print("数据 ", cmd[i])
            print("串口发出{}个字节。".format(write_len))
            time.sleep(3.5)

    def setArmAngleByKeyboard(self):
        angle = self.angleToHex(self.perAngle * self.controlCount[self.currentPinOfLead])
        l = str(self.currentPinOfLead)
        if len(l)==1:
            l = "0"+l
        cmd = bytes.fromhex("ff 02 {} {}".format(l,angle))
        write_len = self.ser.write(cmd)
        print("数据 ", cmd)
        print("串口发出{}个字节。".format(write_len))

    def findPorts(self):
        ports_list = list(serial.tools.list_ports.comports())  # 获取所有串口设备实例。
        if len(ports_list) <= 0:  # 如果没找到串口设备，则输出：“无串口设备。”
            print("无串口设备。")
        else:
            print("可用的串口设备如下：")  # 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
            for comport in ports_list:
                print(list(comport)[0], list(comport)[1])

    def initSerial(self, portName):
        self.findPorts()
        ser = serial.Serial(port=portName,
                            baudrate=115200,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            timeout=None)
        if ser.isOpen():  # 判断串口是否成功打开
            print("打开串口成功。")
            print(ser.name)  # 输出串口号
            self.ser = ser
        else:
            print("打开串口失败。")

    def angleToHex(self,angle):
        num = int((angle / 180) * 2000) + 500
        # print("num ",num)
        val = hex(num)[2:]
        if (len(val) == 1):
            val = '000' + val
        elif (len(val) == 2):
            val = '00' + val
        elif (len(val) == 3):
            val = '0' + val
        val2 = val[2:4] + " " + val[:2]
        return val2

    def getLeadOfPinAllCmd(self, leadOfPin):
        cmd = []
        for i in range(180 // self.perAngle + 1):
            angle = self.angleToHex(self.perAngle * i)
            val = "ff 02 {}".format(leadOfPin) + " " + angle
            cmd.append(bytes.fromhex(val))
        return cmd

    def testArmAllAngle(self, leadOfPin, sleepTime):
        cmd = self.getLeadOfPinAllCmd(leadOfPin)
        for i in range(len(cmd)):
            write_len = self.ser.write(bytes.fromhex(cmd[i]))
            print("数据 ", cmd[i])
            print("串口发出{}个字节。".format(write_len))
            time.sleep(sleepTime)


# cmd = [bytes.fromhex("ff 02 07 00 00"),bytes.fromhex("ff 02 07 e8 03"),bytes.fromhex("ff 02 07 c4 09")]


# 监听键盘按下up、down
# key_listener = test.KeyListener()
# key_listener.start()
# ser = getReadySerial()
# cmd = getAllCmd("04",20)
# clip(ser,cmd)
# ser.write(cmd[0])


con1 = armControl()
# 初始化串口通信设备为COM3
con1.initSerial("COM3")
# 设置通过键盘按键控制机械臂，数字键设置引脚，up键增加角度，down键减小角度
con1.controlArmsByKeyboard()
# 设置机械臂每次转动的角度
con1.setArmPerAngle(1)
# 将04引脚对应的机械臂从0°转动到180°
# con1.testArmAllAngle("04",1)


# while True:
#     com_input = ser.read(10)
#     if com_input:  # 如果读取结果非空，则输出
#         print(com_input)

# ser.close()