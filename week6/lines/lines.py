import sys
count=int(0)
if len(sys.argv)<2:sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):sys.exit("Not a Python file")
try: 
    with open(f"{sys.argv[1]}") as file:
        for line in file:
            if not(line.strip()=="" or line.strip().startswith("#")):count+=1
except FileNotFoundError:sys.exit("File does not exist")
print(count)