def main():
    while True:
        try:
            percentage=convert(input("输入输入 "))
            break
        except (ValueError,ZeroDivisionError):pass
        #异常类型组合
    print(gauge(percentage))
def convert(fraction):   
    try:
        X,Y=fraction.strip().split('/')
        X,Y=int(X),int(Y)
        if (X>Y or X<0 or Y<0):raise ValueError
    except ValueError:raise ValueError
    try:return round(X / Y * 100)
    except ZeroDivisionError:raise ZeroDivisionError
def gauge(percentage):
    if percentage>=99:say="F"
    elif percentage<=1:say="E"
    else:say=(f"{percentage}%")
    return say
if __name__ == "__main__":
    main()