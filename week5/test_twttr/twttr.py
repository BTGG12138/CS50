"""
say=input("输入输入 ").strip()
dont=("a","e","i","o","u")
for letter in dont:
    say=say.replace(letter.upper(),"").replace(letter.lower(),"")
    #对象可以链式调用
print(say)
"""

def main():
    print(shorten(word=input("输入输入 ").strip()))
def shorten(word):
    dont=("a","i","o","u")
    for letter in dont:
        word=word.replace(letter.upper(),"").replace(letter.lower(),"")
    return word  
if __name__ == "__main__":
    main()