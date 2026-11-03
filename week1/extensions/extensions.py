say=input("输入输入 ").strip().lower()
if say.endswith((".gif",".png",)):
    say,what=say.split('.')
    print("image",'/',what,sep='')
elif say.endswith((".jpeg",".jpg")):
    say,what=say.split('.')
    print("image",'/',"jpeg",sep='')
elif say.endswith((".pdf",".zip")):
    say,what=say.split('.')
    print("application",'/',what,sep='')
elif say.endswith(("txt")):
    print("txt.plain")
else:
    print("application/octet-stream")