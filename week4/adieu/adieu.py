#In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 𝑛
#names with 𝑛 −1
#commas and one and, as in the below:
#在名为 adieu.py 的文件中，编写一个程序。该程序会提示用户输入姓名，每行一个姓名，直到用户输入控制键“D”。假设用户至少会输入一个姓名。然后，将这些姓名按顺序输出，用两个 and 分隔两个姓名，用三个 and 分隔三个姓名，用 𝑛
#和 𝑛 −1 分隔四个姓名，最后用 and 分隔最后一个姓名，
says=[]
while True:
    try:says.append(input("输入输入 "))
    except EOFError:break
print("Adieu, adieu, to ",end='')
if len(says)>=3:
    for say in says:
        if say==says[-2]:
            #len()从0开始计数,长度是长度
            print(f"{say}, and {says[-1]}")
            #says[-1]是最后一个
            break
        else:print(say,end=', ')
elif len(says)==2:print(f"{says[0]} and {says[1]}")
else:print(says[0])