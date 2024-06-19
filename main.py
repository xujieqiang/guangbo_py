import os
import selectmusic

import selecttime
import selectgroups
print("开始生成广播系统指令！")
print("==================")
print("逐条生成指令\n 在生成指令之前先设置这个方案的名称，\n然后再逐条输入指令！")
print("=============")
# 方案名称确立
print()
fangan=input("请输入一个方案的名称：")

onerecord=[]
# 铃声名称
name=input("输入铃声的名称：")
onerecord.append(name)

#jobtype
onerecord.append(2)
#jobmask
onerecord.append(0)

#duration
onerecord.append(0)
# 设置时间
starttime=selecttime.setagain()
onerecord.append(starttime)
print(f"设置的时间是：  {onerecord}")

#stoptime
onerecord.append('2023-10-10')
# jobdata
onerecord.append(65663)
# repeatnum
onerecord.append(1)
#playmode
onerecord.append(0)
#playvol
onerecord.append(0)
# 设置音频文件
selectedpath=selectmusic.selectp()
print()
print(f"选择的文件夹是：{selectedpath}")
print()
medias=selectmusic.selectf(selectedpath)
onerecord.append(medias)

# terms
onerecord.append('')
# areamask
onerecord.append('')
# 选择 groups
groups=selectgroups.setgroups()
onerecord.append(groups)
# poweraheadplay
onerecord.append('')
print(onerecord)