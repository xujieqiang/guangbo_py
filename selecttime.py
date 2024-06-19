
def settime():
    prefix='2023-10-10'
    t=input("请输入：：开始时间")
    last=prefix+" "+t
    return last

def setagain():
    t=''
    while True:
        t=settime()
        confirm=input("是否确认：  y  or n")
        if confirm=='y'  or confirm=='Y':
            break
    return t

