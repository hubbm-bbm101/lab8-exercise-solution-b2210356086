import sys
student,university=[],[]
content=open(sys.argv[1],"r",encoding="UTF-8")
for line in content:
    line=line.rstrip()
    student.append(line.split(":")[0]),university.append(line.split(":")[1])
stu_to_uni=dict(zip(student,university))
commands=sys.argv[2].split(",")
for name in commands:
    try:
        print("Name: "+name+", University: "+stu_to_uni[name])
    except KeyError:
        print("No record of '"+name+"' was found!")