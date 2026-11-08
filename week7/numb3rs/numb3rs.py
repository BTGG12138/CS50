def main():print(validate(input("IPv4 Address: ")))
def validate(ip):
    try:
        parts= ip.strip().split(".")
        if len(parts)!=4:return False
        else:
            for i in parts:
                if not (0<=int(i)<=255 and i.isdigit() and str(int(i))==i):return False
        return True
    except (ValueError,SyntaxError):return False
if __name__ == "__main__":
    main()
