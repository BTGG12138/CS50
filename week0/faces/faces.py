#In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
#在一个名为 faces.py 的文件中，实现一个名为 convert 的函数。该函数接受一个 str 类型的输入，并将该输入进行如下转换：所有 :) 类型的元素将被转换为 🙂 类型（即呈现为略带微笑的表情），所有 :( 类型的元素将被转换为 🙁 类型（即呈现为略带皱眉的表情）。其他所有文本内容则保持不变。

#Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.
#然后，在同一个文件中，实现一个名为 main 的函数。该函数会提示用户输入，根据用户输入调用 convert 函数，并输出结果。如果你愿意，也可以直接通过向 input 函数传递自己的参数 str 来提示用户输入。请确保在文件的底部调用 main 函数。
def convert(face):
    face=face.replace(":)","🙂")   
    face=face.replace(":(","🙁")
    #要赋值
    return face
    #没有返回值不会报错
def main():
    print(convert(input("输入输入 ")))
if __name__=="__main__":
    main()