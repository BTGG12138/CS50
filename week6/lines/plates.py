#“All vanity plates must start with at least two letters.”
#“所有的车牌都必须以至少两个字母开头。”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“……虚荣牌上最多可以包含 6 个字符（字母或数字），最少则需要 2 个字符。”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“数字不能放在车牌的中间位置，必须放在末尾。例如，AAA222 就是一个合法的车牌组合；而 AAA22A 则是不被允许的。第一个使用的数字不能为‘0’。”
#“No periods, spaces, or punctuation marks are allowed.”
#“不允许使用标点符号、空格或任何符号。”
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #.isalnum() 是不是字母或者数字
    #.isalpha() 只判断字母
    #.isdigit() 只判断数字
    if not s.isalnum():return False
    if (len(s)<2 or len(s)>6):return False
    for first_num in s:
        #三元表达式内只能赋值
        if first_num.isdigit():
            if first_num=="0":return False
            letter,nums=s.split(first_num,1)
            for num in nums:
                if num.isalpha():return False
            break
    if not (s[0].isalpha() and s[1].isalpha()):return False
    return True
main()