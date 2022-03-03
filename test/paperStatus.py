#把接收到的狀態打印出來
from ser import paper_status
p = "printer status: "
if paper_status == "12":
    print(p+"paper adequate")
elif paper_status == "1e":
    print(p+"Paper roll end detected by paper roll sensor")
elif paper_status == "72":
    print(p+"Paper near-end is detected by the paper roll near-end sensor.")
elif paper_status == "7e":
    print(p+"both sensor detected paper roll end")
else:
    print("other status:",paper_status)
    
