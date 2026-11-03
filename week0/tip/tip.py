#dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
#dollars_to_float ，该表达式应接受 str 作为输入（格式为 $##.## ，其中每个 # 表示一个十进制数字），去掉前面的 $ ，然后将结果返回为 float 。例如，当输入为 $50.00 时，它应该返回 50.0 。
#percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
#percent_to_float ，该变量应接受 str 作为输入（格式为 ##% ，其中每个 # 表示一个十进制数字），去掉末尾的 % ，然后将百分比作为 float 返回。例如，当输入为 15% 时，它应该返回 0.15 。
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$",""))


def percent_to_float(p):
    return float(p.replace("%",""))*0.01


main()