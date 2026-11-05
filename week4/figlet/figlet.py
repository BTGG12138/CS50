"""
cd /home/btgg/Desktop/CS50/week4/figlet && \
[ -d .venv ] || python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyfiglet && \
python -c "import pyfiglet; print('安装成功:', pyfiglet.__file__)"
"""

"""
# 基本用法：使用指定字体
pyfiglet -f slant "Hello, World!"
# 指定输出宽度
pyfiglet -f doom "TEXT" -w 80
# 查看所有可用字体(pyfiglet 内置了超过 500 种字体)
pyfiglet --list_fonts
"""
import sys
import random
import pyfiglet


def main():
    fonts = pyfiglet.FigletFont.getFonts()
    #获取pyfiglet支持的所有字体
    if len(sys.argv) == 1:font = random.choice(fonts)
    #随机随机
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        font = sys.argv[2]
        if font not in fonts:sys.exit("Invalid usage")
        #sys.exit("文本")
    else:
        sys.exit("Invalid usage")
    print(pyfiglet.Figlet(font=font).renderText(input()))
    #左边font=函数/类定义里的参数名
    #右边font=你代码里的变量名
    #f = pyfiglet.Figlet(font=font)   
    #text = input()                   
    #art = f.renderText(text)         
    #print(art)                       
if __name__ == "__main__":
    main() 
"""
cd /home/btgg/Desktop/CS50/week4/figlet
pip freeze > requirements.txt    # 必须在激活状态下执行
deactivate
rm -rf .venv
"""