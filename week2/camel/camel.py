say=input("输入输入 ").strip()
for letter in say:
    if letter.isupper():
        say=say.replace(letter,"_"+letter.lower()) 
print(say)
        