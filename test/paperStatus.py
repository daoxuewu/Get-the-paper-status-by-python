from ser import paper_status
p = "印表機紙捲狀態:"
if paper_status == "12":
    print(p+"紙捲狀態正常")
elif paper_status == "1e":
    print(p+"下方探測器缺紙")
elif paper_status == "72":
    print(p+"上方探測器缺紙")
elif paper_status == "7e":
    print(p+"上下都沒紙了")
else:
    print("其他未設定狀態:",paper_status)
    
