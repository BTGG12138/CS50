"""
    Expects the user to provide two command-line arguments:
    期望用户提供两个命令行参数：
        the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
        需要作为输入的已存在 CSV 文件的名称。该文件的列顺序依次为 name 和 house 。
        the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
        一个新的 CSV 文件的名称，该文件作为输出结果使用。该文件的列顺序应为： first 、 last 、 house 。
    Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
    将这些输入数据转换为相应的输出数据，将每个 name 元素分别拆分为一个 first 名称和一个 last 名称。假设每个学生都有名字和姓氏。
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
如果用户提供的不完全是两个命令行参数，或者第一个参数无法被读取，那么程序应该以错误消息退出，并提示 sys.exit 错误。
"""
import csv
import sys
lis=[]
if len(sys.argv)<3:sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:sys.exit("Too many command-line arguments")
if not (sys.argv[1].endswith(".csv") and sys.argv[1].endswith(".csv")) :sys.exit("Not a CSV file")
try: 
    with open(f"{sys.argv[1]}") as file:
        reader=csv.reader(file)
        next(reader)
        #跳过表头
        for row in reader:
            first,last=row[0].split(", ")
            lis.append([first,last,row[1]])
except FileNotFoundError:sys.exit(f"Could not read {sys.argv[1]}.csv")
with open("after.csv",'w') as file:
    writer=csv.writer(file)
    writer.writerows(lis)
    #反正就是writer