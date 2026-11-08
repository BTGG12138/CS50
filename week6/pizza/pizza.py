#cd /home/btgg/Desktop/CS50/week6/pizza && python3 -m venv .venv && source .venv/bin/activate && pip install tabulate && pip show tabulate
#print(tabulate(rows, headers="firstrow", tablefmt="grid"))
"""
data = [
    ["Cheese",  "$25.50", "$39.95"],
    ["1 item",  "$27.50", "$41.95"],
    ["2 items", "$29.50", "$43.95"],
    ["3 items", "$31.50", "$45.95"],
    ["Special", "$33.50", "$47.95"],
]
print(tabulate(
    data,
    headers=["Sicilian Pizza", "Small", "Large"],
    tablefmt="grid"
))
"""
import sys
import csv
import tabulate
lis=[]
if len(sys.argv)<2:sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):sys.exit("Not a CSV file")
try: 
    with open(f"{sys.argv[1]}") as file:
        reader=csv.reader(file)
        #csv.reader 的作用是：把 CSV 文件里一行行“按逗号分隔的纯文本字符串”，自动切分并转换成 Python 的“列表（List）”
        for row in reader:lis.append(row)
    print(tabulate.tabulate(lis, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:sys.exit("File does not exist")
#deactivate