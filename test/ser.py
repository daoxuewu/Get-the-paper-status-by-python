import serial   
import serial.tools.list_ports
import sys
import glob

# 開啟串列埠，並得到串列埠物件 (Serial port 又稱序列埠、串列連線埠、串口)
serialPort = serial.Serial(
    port="COM2",      #請自行視連接方式修改參數
    baudrate=115200,  #設定鮑率(每秒鐘傳符號率)
    bytesize=8,       #data type 8bit
    parity="N",       #同位檢查(一般不使用)
    stopbits=1,       #停止位：是在每個位元組傳輸之後傳送的，它用來幫助接受訊號方硬體重同步。
    timeout=1.00)   

# ser=serial.Serial("/dev/ttyUSB0",9600,timeout=0.5) #使用USB連線串列埠
# ser=serial.Serial("/dev/ttyAMA0",9600,timeout=0.5) #使用樹莓派的GPIO連線串列埠
# ser=serial.Serial(1,9600,timeout=0.5)#winsows系統使用com1口連線串列埠
# ser=serial.Serial("com1",9600,timeout=0.5)#winsows系統使用com1連線串列埠
# ser=serial.Serial("/dev/ttyS1",9600,timeout=0.5)#Linux系統使用com1連線串列埠

# print("正在連接的列埠詳細資訊:",serialPort)
print("串列埠是否打開:",serialPort.is_open)
print("正在連接的串列埠:",serialPort.port)

#寫入16進制資料
writeHex = serialPort.write(b'\x10\x04\x04')
print("總寫入位元組數:",writeHex)

#十六進位制的讀取
paper_status = serialPort.read().hex() #ser.read(20) 是讀20個字元的意思 
print("印表機紙捲的狀態:",paper_status)  #ser.readline() #是讀一行，以/n結束，要是沒有/n就一直讀，阻塞，需要設定超時時間!

#當前可用的所有 serial port 的列表
comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)
print("當前可用的所有 COM ports: " + str(connected))
# print("正在使用的 COM port:",element)

#取得剩那些通訊串列埠還沒被用
def available_port():
    #自動判斷作業系統
    if sys.platform.startswith('win'):
    # !attention assumes pyserial 3.x
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
    # ios/macos
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('不支援的平台')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
# print("尚未被使用的 COM Ports: " + str(result))
print("尚未被使用的 COM Ports: ",available_port())

print("---------------")
serialPort.close()#關閉串列埠