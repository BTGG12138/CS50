say=input("输入输入 ").strip()
if ' + ' in say:
    num1,num2=say.split(' + ')
    print(float(num1)+float(num2))
elif ' - ' in say:
    num1,num2=say.split(' - ')
    print(float(num1)-float(num2))
elif ' * ' in say:
    num1,num2=say.split(' * ')
    print(float(num1)*float(num2))
else:
    num1,num2=say.split(' / ')
    print(float(num1)/float(num2))