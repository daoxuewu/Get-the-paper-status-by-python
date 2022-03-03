# Get_printer_paper_status

最近工作上突然被指派一個任務是去寫個程式來偵測印表機的狀態(是否有缺紙)結合line notify推撥訊息，但網路上查python在這方面的相關資源實在是很少，於是完成後我把程式放在這希望之後可以幫助到有需要的人，適用於支援 ESC/POS 指令的印表機，程式中含有詳細註解可以幫助理解，若有任何問題歡迎和我聯繫。

使用 python 的 [pySerial](https://pypi.org/project/pyserial/) 模組進行序列通訊，取得印表機紙捲的狀態。

Using [pySerial](https://pypi.org/project/pyserial/) to get the paper status of escpos printers.

## Installation
``pip install pyserial`` should work for most users.

Detailed information can be found in [pySerial installation](https://github.com/pyserial/pyserial/blob/master/documentation/pyserial.rst#installation).

## References
- pySerial’s documentation : https://pyserial.readthedocs.io/en/latest/
- ESC/POS Command Set : https://aures-support.com/DATA/drivers/Imprimantes/Commande%20ESCPOS.pdf
- EPSON : https://reference.epson-biz.com/modules/ref_escpos/index.php

## Tested printers
- APPOSTAR KPM-2520

## License
Mit License Copyright (c) 2022 Daoxue Wu