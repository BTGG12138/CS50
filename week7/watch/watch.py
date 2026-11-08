import re
def main():print(parse(input("HTML: ")))
def parse(s):
    if say:=re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([^"?]+)',s):
        return f"https://youtu.be/{say.group(1)}"
    #?          前面的内容，重复 0 次或 1 次
    #(?:...)    叫非捕获分组。括号的作用是“把一串东西打包成一个整体”，方便后面加量词或做或运算：
    #[^"?]      的意思是：一直吃字符，直到遇到引号或问号就停。
    #捕获组正则表达式应该用的可选的字母s非捕获组\.表达式？出现一次或者两次同时取反"和?至少一个
    else:return None
if __name__ == "__main__":
    main()
