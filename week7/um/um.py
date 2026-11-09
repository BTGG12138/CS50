import re
def main():print(count(input("Text: ")))
def count(s):
    count=len(re.findall(r'\bum\b',s,re.IGNORECASE))
    #\b 在某个位置成立，当且仅当该位置左右两侧"单词性"不同：
    return count
if __name__ == "__main__":main()