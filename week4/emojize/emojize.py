"""
我也不知道
sudo apt update && \
sudo apt install -y python3.14-venv && \
cd /home/btgg/Desktop/CS50/week4/emojize && \
rm -rf .venv && \
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple emoji && \
python -c "import emoji; print('安装位置:', emoji.__file__)" && \
python emojize.py
"""

"""
import emoji

# 将 emoji 代码转换为表情符号
print(emoji.emojize('Python is :thumbs_up:'))
# 输出: Python is 👍

# 使用别名
print(emoji.emojize('Python is :thumbsup:', language='alias'))
# 输出: Python is 👍

# 将表情符号转换回代码
print(emoji.demojize('Python is 👍'))
# 输出: Python is :thumbs_up:

# 使用变体（显示彩色心形）
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# 输出: Python is fun ❤️

# 检查是否为 emoji
print(emoji.is_emoji("👍"))  # True
"""

"""
cd /home/btgg/Desktop/CS50/week4/emojize
pip freeze > requirements.txt    # 必须在激活状态下执行
deactivate
rm -rf .venv
"""
import emoji
say = input("Input: ")
print(emoji.emojize(say, language='alias'))