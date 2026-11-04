while True:
    try:
        X,Y=input("输入输入 ").strip().split('/')
        X=int(X)
        Y=int(Y)
        if X<=Y:
            num=round(float(X/Y)*100)
            break
    except ValueError or ZeroDivisionError:
        pass
if num>=99:
    print("F")
elif num<=1:
    print("E")
else:
    print(num,"%",sep='')