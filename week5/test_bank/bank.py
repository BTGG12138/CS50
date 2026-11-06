"""
#In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
#在名为 bank.py 的文件中，实现一个程序，提示用户进行问候。如果问候以“hello”开头，输出 $0 。如果问候以“h”开头（但不以“hello”）开头，输出 $20 。否则，输出 $100 。忽略用户问候语中的前置空白，并对用户的问候语进行无关紧要的处理。
say=input("输入输入 ").strip().lower()
if  say.startswith("hello"):
    #检测字符串首字母的
    print("0$")
else:
    print("20$") if say.startswith("h") else print("100$")
"""

def main():print(f"{value(input("输入输入 ").strip().lower())}$")
def value(greeting):
    if  greeting.startswith("hello"):return int(0)
    else:
        if greeting.startswith("h"): return int(20) 
        else: return int(10)
if __name__ == "__main__":
    main()