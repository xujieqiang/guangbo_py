import onerecord
import xlwt
print("开始生成广播系统指令！")
print("==================")
print("逐条生成指令\n 在生成指令之前先设置这个方案的名称，\n然后再逐条输入指令！")
print("=============")
# 方案名称确立
print()
fangan = input("请输入一个方案的名称：")

# 创建excel
workbook=xlwt.Workbook(encoding='utf-8')
sheet=workbook.add_sheet(fangan)


columns=['Name','JobType','JobMask','Duration','StartTime','StopTime',
         'JobData','RepeatNum','PlayMode','PlayVol','Medias','Terms','AreaMasks',
         'Groups','PowerAheadPlay']
for col,column in enumerate(columns):
    sheet.write(0,col,column)

def displayrs(list):

    print("name            ,        starttime              ,               medias                 ,    groups")
    for i,rowval in enumerate(list):
        name=''
        starttime=''
        medias=''
        groups=''

        for j,val in enumerate(rowval):
            if j==0:
                name=val
            if j==4:
                starttime=val
            if j==10:
                medias=val
            if j==13:
                groups=val
        print(f"{name}              ,     {starttime}       ,   {medias}    ,        {groups} ")



total=[]
while True:
    od=onerecord.generateonerecord()
    total.append(od)
    displayrs(total)

    c=input("继续添加另外一条记录吗？y  or  n")
    if c!='y'  and c!='Y':
        break


for i ,row in enumerate(total):
    for j,colval in enumerate(row):
        sheet.write(i+1,j,colval)


workbook.save('./xx.xls')