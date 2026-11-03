#In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
#在名为 playback.py 的文件中，用 Python 编写一个程序。该程序会提示用户输入一些内容，然后输出经过处理的输入结果，其中所有的空格都会被替换为 ... （即三个点）。
say=input("输入输入 ")
print(say.replace(" ", "..."))
#str.replace(old, new[, count])