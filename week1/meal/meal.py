def main():
    time=convert(input("输入输入 "))
    if 7.0<=time<=8.0:
        print("breakfast time")
    elif 12.0<=time<=13.0:
        print("lunch time")
    elif 18.0<=time<=19.0:
        print("dinner time")
    else:
        pass
def convert(time):
    if time.endswith("a.m."):
        time=time.replace(" a.m.","")
        hour,minute=time.split(':')
        time=float(hour)+float(minute)/60
    elif time.endswith("p.m."):
        time=time.replace(" p.m.","")
        hour,minute=time.split(':')
        time=float(hour)+12+float(minute)/60
    else:
        hour,minute=time.split(':')
        time=float(hour)+float(minute)/60
    return time
if __name__ == "__main__":
    main()