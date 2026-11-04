dic={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total=float(0.0)
while True:
    say=input("输入输入 ").strip()
    if say=='D':break
    for name in dic:
        if say.casefold()==name.casefold():
            total+=float(dic[name])
            #反正反正
            print(f"Total: ${total:.2f}")