import os
import selectmusic

import selecttime
import selectgroups



def generateonerecord():
    onerecord = []
    # 铃声名称
    name = input("输入铃声的名称：")
    onerecord.append(name)

    # jobtype
    onerecord.append(2)
    # jobmask
    onerecord.append(0)

    # duration
    onerecord.append(0)
    # 设置时间
    starttime = selecttime.setagain()
    onerecord.append(starttime)
    print(f"设置的时间是：  {onerecord}")

    # stoptime
    onerecord.append('2023-10-10')
    # jobdata
    onerecord.append(65663)
    # repeatnum
    onerecord.append(1)
    # playmode
    onerecord.append(0)
    # playvol
    onerecord.append(0)
    # 设置音频文件
    selectedpath = selectmusic.selectp()
    print()
    print(f"选择的文件夹是：{selectedpath}")
    print()
    medias = selectmusic.selectf(selectedpath)
    onerecord.append(medias)

    # terms
    onerecord.append('')
    # areamask
    onerecord.append('')
    # 选择 groups
    groups = selectgroups.setgroups()
    onerecord.append(groups)
    # poweraheadplay
    onerecord.append(0)
    return onerecord