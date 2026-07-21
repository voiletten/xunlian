students = []
for i in range(5):
    print(f"请输入第{i+1}学生信息")
    a = input("姓名")
    b = input("学号")
    fs = float(input("第一门"))
    ss = float(input("第二门"))
    ts = float(input("第三门"))
    avg = round((fs + ss + ts)/3,2)
    students.append([a,b,fs,ss,ts,avg])
with open("stud","w",encoding="utf-8") as f:
    f.writelines("f{'学号':<10}{'姓名':<10}{'成绩1':<8}{'成绩2':<8}{'成绩3':<8}{'平均分'}\n")


    for a,b,fs,ss,ts,avg in students:
        f.write(f"{b:<10}{a:<10}{fs:<8}{ss:<8}{ts:<8}{avg}\n")
