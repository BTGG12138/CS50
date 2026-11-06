import random
def main():
    level=get_level()
    score=int(0)
    for _ in range(1,11):
        #不包含右括号
        x,y=generate_integer(level)
        for i in range(1,4):
            try:
                print(x,"+",y,"= ",end="")
                say=int(input())
                if (i==3 and say!=(x+y)):print(x,"+",y,"=",x+y)
                elif say!=(x+y):print("EEE")
                else: 
                    score+=1  
                    break
            except ValueError:print("EEE")
    print("Score:",score)
def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1<=level<=3:return level
        except ValueError:pass
def generate_integer(level):
    x=random.randint(1,10**level)
    y=random.randint(1,10**level)
    return x,y
if __name__ == "__main__":
    main()