''' expression 的返回值會給 variable
=============================
with "expression" as "variable":
    ....
=============================
1. file.readline()：返回一行。
2. for line in file: print line ：通過迭代器存取。
3. f.close() : 關閉文件
'''

with open('blablabla.txt', "r") as file:
    # file 的型別
    print(type(file))

    # 讀取第一行
    a = file.readline()
    print("a: ", a)

    # 從第二行開始讀取
    i = 1
    for line in file:
        print(f'line {i}: {line}')
        i += 1