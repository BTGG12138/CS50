import re
import sys
def main():print(convert(input("Hours: ")))
def convert(s):
    if say:=re.fullmatch(r'(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)',s):
        #空格是\s\d只能捕获一个数字转用{}
        beforeh,beforem,beforeM,afterh,afterm,afterM=say.groups()
        if beforem==None:beforem="00"
        if afterm==None:afterm="00"
        if not (0<=int(beforeh)<=12 and 0<=int(afterh)<=12 and 0<=int(beforem)<=59 and 0<=int(afterm)<=59):raise ValueError
        if beforeM=="PM":beforeh=int(beforeh)+12
        elif 0<=int(beforeh)<=9:beforeh=f"0{beforeh}"
        if afterM=="PM":afterh=int(afterh)+12
        elif 0<=int(afterh)<=9:afterh=f"0{afterh}"
        return f"{beforeh}:{beforem} to {afterh}:{afterm}"
    else:raise ValueError
    #?          前面的内容，重复 0 次或 1 次
    #(?:...)    叫非捕获分组。括号的作用是“把一串东西打包成一个整体”，方便后面加量词或做或运算：
    #[^"?]      的意思是：一直吃字符，直到遇到引号或问号就停。
    #捕获组正则表达式应该用的可选的字母s非捕获组\.表达式？出现一次或者两次同时取反"和?至少一个
if __name__ == "__main__":main()