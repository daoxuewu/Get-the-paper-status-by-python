import serial
import serial.tools.list_ports

# 開啟串列埠(Serial port)，並得到串列埠物件 
serialPort = serial.Serial(
    port="COM2",
    baudrate=115200,
    bytesize=8,
    parity="N", 
    stopbits=1,
    timeout=1.00)

#寫入16進制資料
ans = serialPort.write(b'\x10\x04\x04')
#十六進位制的讀取
paper_status = serialPort.read().hex()
#關閉串列埠
serialPort.close()