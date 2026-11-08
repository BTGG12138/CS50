"""
from PIL import Image
bg = Image.open("background.jpg").convert("RGBA")
fg = Image.open("logo.png").convert("RGBA")
# 1. 改大小：按比例缩放
scale = 0.3
new_size = (int(fg.width * scale), int(fg.height * scale))
fg = fg.resize(new_size, Image.LANCZOS)
# 也可以缩放到固定尺寸
# fg = fg.resize((200, 120), Image.LANCZOS)
# 2. 改位置：先把 PNG 贴到同尺寸透明画布上
canvas = Image.new("RGBA", bg.size, (0, 0, 0, 0))
position = (50, 80)          # 左上角坐标
canvas.paste(fg, position, fg)   # 第三个参数用 fg 做 mask，保留透明
# 3. 合成
result = Image.alpha_composite(bg, canvas)
result.convert("RGB").save("output.jpg", quality=95)
"""
from PIL import Image
import sys
if len(sys.argv)<3:sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:sys.exit("Too many command-line arguments")
if not (sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".png")) :sys.exit("Not a Right file")
back=Image.open((sys.argv[1])).convert("RGBA")
front=Image.open((sys.argv[2])).convert("RGBA")
front=front.resize((back.width,int(back.height*1.5)),Image.LANCZOS)
canvas = Image.new("RGBA", back.size, (0, 0, 0, 0))
canvas.paste(front,(0,-800),front)
result = Image.alpha_composite(back, canvas)
result.convert("RGB").save("output.jpg", quality=95)