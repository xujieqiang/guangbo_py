import os




def selectp():
    file_path = "D:\\系统铃声"

    p = os.walk(file_path)
    dirlist = []
    for root, dirs, files in p:
        for dname in dirs:
            dl = os.path.join(root, dname)
            dirlist.append(dl)
        break


    for i, v in enumerate(dirlist):
        print(f"[{i + 1}] {v}")
    print()

    pos = (input("请输入序号，选择相应的文件位置："))
    while not (pos.isdigit()):
        print("你输入的不正确！")
        pos = (input("请输入序号，选择相应的文件位置："))
    maxlen = len(dirlist)
    pos1 = int(pos)
    while pos1 < 1 or pos1 > maxlen:
        print("数字越界// 非整数")
        pos1 = int(input("请输入序号，选择相应的文件位置："))
    filepath1 = dirlist[pos1 - 1]
    print ('=================================>')
    print(f"你所选择的路径是：===>{filepath1}")
    print('=================================>')
    print( )

    selectedpath= filepath1

    return selectedpath



def diplayfiles(path):
    p1 = os.walk(path)
    rlist = []
    for root, dirs, files in p1:
        for dname in files:
            dl = os.path.join(root, dname)
            rlist.append(dl)
    return rlist



def selectf(path):
    filelist=diplayfiles(path)
    selectedfile=''

    for i, v in enumerate(filelist):
        print(f"[{i + 1}] {v}")
    print()
    pos = (input("请输入序号，选择相应的文件位置："))
    while not (pos.isdigit()):
        print("你输入的不正确！")
        pos = (input("请输入序号，选择相应的文件位置："))
    maxlen = len(filelist)
    pos1 = int(pos)
    while pos1 < 1 or pos1 > maxlen:
        print("数字越界// 非整数")
        pos1 = int(input("请输入序号，选择相应的文件位置："))
    filepath1 = filelist[pos1 - 1]
    print(f"你所选择的路径是：===>{filepath1}")
    print()

    selectedfile = filepath1

    return selectedfile