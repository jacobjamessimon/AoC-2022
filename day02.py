lines=[]
with open("C:\\Users\\Jacob\\AoC\\day02.txt") as f:
    lines=f.readlines()
points=0
for line in lines:
    if line[0]=="A": #rock
        if line[2]=="X":#lose
            points+=3
        elif line[2]=="Y":#draw
            points+=4
        elif line[2]=="Z":#W
            points+=8
    if line[0]=="B": #paper
        if line[2]=="X":
            points+=1
        elif line[2]=="Y":
            points+=5
        elif line[2]=="Z":
            points+=9
    if line[0]=="C": #scissors
        if line[2]=="X":
            points+=2
        elif line[2]=="Y":
            points+=6
        elif line[2]=="Z":
            points+=7
print(points)