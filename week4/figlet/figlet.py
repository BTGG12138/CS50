"""
cd /home/btgg/Desktop/CS50/week4/figlet && \
[ -d .venv ] || python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyfiglet && \
python -c "import pyfiglet; print('安装成功:', pyfiglet.__file__)"
"""
import pyfiglet
