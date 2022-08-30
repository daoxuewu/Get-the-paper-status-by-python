# Get the paper status by python

最近工作上突然被指派一個任務是去寫個程式來偵測印表機的狀態(是否有缺紙)結合line notify推撥訊息，但網路上查python在這方面的相關資源實在是很少，本來不想再花時間造輪子的，但剛好 [python-escpos](https://github.com/python-escpos/python-escpos) 這個library [沒有implement讀取紙張狀態這個功能](https://github.com/python-escpos/python-escpos/issues/286)，於是我使用 `pySerial` 來實作這個功能，完成後我把程式放在這希望之後可以幫助到有需要的人，適用於支援 ESC/POS 指令的印表機，程式中含有詳細註解可以幫助理解，若有任何問題歡迎和我聯繫。

使用 python 的 [pySerial](https://pypi.org/project/pyserial/) 模組進行序列通訊，取得印表機紙捲的狀態。

Using [pySerial](https://pypi.org/project/pyserial/) to get the paper status of escpos printers.

## 需求套件 / Requirement
This script requires pyserial library. You can install it easily by:
```
pip install pyserial
```

Detailed information can be found in [pySerial installation](https://github.com/pyserial/pyserial/blob/master/documentation/pyserial.rst#installation).

## ESC/POS 指令介紹
ESC/POS 指令可以傳送三種格式來和印表機進行序列通訊，分別是ASCII、十六進制(Hex)、十進制(Decimal)，照著指令可以進一步去做到控制印表機進行列印、查詢印表機的狀態等等的動作，這次要做的內容是查詢印表機的紙捲狀態(有兩個指令可以查看)，介紹如下: 

第一個是 DLE EOT n (實時查看) 

![image](https://github.com/daoxuewu/Get-the-paper-status-by-python/blob/main/img/DLE_EOT_n.png) 

n = 4 是傳輸紙卷感測器狀態 

![image](https://github.com/daoxuewu/Get-the-paper-status-by-python/blob/main/img/n_4.png)

第二個是 GS r n

![image](https://github.com/daoxuewu/Get-the-paper-status-by-python/blob/main/img/GS_r_n.png)

![image](https://github.com/daoxuewu/Get-the-paper-status-by-python/blob/main/img/n_1_49.png)

## References
- pySerial’s documentation : https://pyserial.readthedocs.io/en/latest/
- ESC/POS Command Set : https://aures-support.com/DATA/drivers/Imprimantes/Commande%20ESCPOS.pdf
- EPSON : https://reference.epson-biz.com/modules/ref_escpos/index.php
- android 控制POS機圖文打印 : https://blog.csdn.net/sdvch/article/details/45096041

## Tested printers
- APPOSTAR KPM-2520

## License
>Mit License Copyright (c) 2022 Daoxue Wu
