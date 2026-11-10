"""
cd /home/btgg/Desktop/CS50/week8/shirtificate
python3 -m venv .venv
source .venv/bin/activate
pip install fpdf2
# 使用清华源安装 fpdf2
pip install fpdf2 -i https://pypi.tuna.tsinghua.edu.cn/simple
# 或者使用阿里云源
pip install fpdf2 -i https://mirrors.aliyun.com/pypi/simple/
"""
"""
from fpdf import FPDF
# 1. 创建画布 (默认 A4 纵向，单位毫米)
pdf = FPDF()
pdf.add_page()  # 添加一页
# 2. 设置字体 (Helvetica 是内置字体，无需额外文件)
pdf.set_font("Helvetica", size=12)
# 3. 添加一个单元格并写入文字
pdf.cell(0, 10, "Hello World!")
# 4. 输出并保存为 PDF 文件
pdf.output("hello.pdf")
pdf.image("path/to/image.png", x, y, w, h)
"""
from fpdf import FPDF
pdf=FPDF()
pdf.add_page()
pdf.image("shirtificate.png",0,50)
pdf.set_font("Helvetica", size=100)
pdf.set_text_color(255, 255, 255)
pdf.cell(0,225,"NMSL",align="C")
#align="C"居中
pdf.output("shirtificate.pdf")