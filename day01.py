lines=[]
with open("C:\\Users\\Jacob\\AoC\\day01.txt") as f:
    lines=f.readlines()
sumlist=[0]
x=0
for idx, line in enumerate(lines):
    if line=="\n":
        x=x+1
        sumlist.append(0)
    else:
        sumlist[x]+=int(line.strip())
print(sorted(sumlist)[-3:])