import csv
say=input("输入输入 ").strip()
with open("fruit_calories.csv",'r') as file:
    reader=csv.DictReader(file)
    #DictReader：直接按表头变成字典
    for line in reader:
        if say.casefold()==line["Fruit"].casefold():
            print("Calories:",line["Calories"])
        #casefold不论大小写