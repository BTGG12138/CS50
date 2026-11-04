lis=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    say=input("输入输入 ")
    if '/' in say:
        month,date,year=say.split('/')
        if 1<=int(date)<=31 and 1<=int(month)<=12:break
    elif ',' in say:
        say=say.replace(',',"")
        month,date,year=say.split(' ')
        if  month in lis and date.isdigit() and year.isdigit():
            month=int(lis.index(month)+1)
            if 1<=int(date)<=31 and 1<=int(month)<=12:
            #字符串：既有 `.find()`，也有 .index()
            #列表：只有.index()，没有.find()！
                break
print(year,month,date,sep='-')
