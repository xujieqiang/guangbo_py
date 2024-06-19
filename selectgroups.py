
def setgroups():
    dict={'初一':'1;','初二':'2;','初三':'3;','全校':'4;','监听调试':'5;',
          '行政楼、科技类':'7;','室外广播':'8;'}
    for k,item in dict.items():
        print(f"{item}\t {k} ")
    print()
    sg=input('请输入1；  2； ……')
    return sg
