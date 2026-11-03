total=int(0)
while total<50:
    print("Amount Due:",50-total)
    push=input("输入输入 ")
    if push in ("5","10","25"):
        total+=int(push)
if total>50.0:
    print("Change Owed:",total-50)