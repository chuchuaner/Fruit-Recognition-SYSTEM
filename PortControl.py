#作业讲解
#讨论水果识别需求,识别到水果后机械臂做什么动作
#串口配置
import serial
import serial.tools.list_ports
def findPorts():
    ports_list = list(serial.tools.list_ports.comports())   # 获取所有串口设备实例。
    if len(ports_list) <= 0:                                # 如果没找到串口设备，则输出：“无串口设备。”
        print("无串口设备。")
    else:
        print("可用的串口设备如下：")                           # 如果找到串口设备，则依次输出每个设备对应的串口号和描述信息。
        for comport in ports_list:
            print(list(comport)[0], list(comport)[1])
findPorts()
ser = serial.Serial(port="COM2",
                    baudrate=115200,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=None)
if ser.isOpen():                        # 判断串口是否成功打开
    print("打开串口成功。")
    print(ser.name)    # 输出串口号
else:
    print("打开串口失败。")
# while True:
print(bytes.fromhex("ff 02 06 f4 01"))
write_len = ser.write(bytes.fromhex("ff 02 05 f4 01"))

print("串口发出{}个字节。".format(write_len))
while True:
    com_input = ser.read(10)
    if com_input:  # 如果读取结果非空，则输出
        print(com_input)

ser.close()