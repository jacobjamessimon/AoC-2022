def main():
    lines=[]
    with open("C:\\Users\\Jacob\\AoC\\day09.txt") as f:
        lines=f.readlines()
    klist=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    s=[0,0]
    tgone=[]
    for line in lines:
        if line[0]=="U":
            for y in range(int(line[2:])):
                for x in range(1,len(klist)):
                    hpos=klist[x-1]
                    tpos=klist[x]
                    if (hpos[1]-tpos[1])==1:
                        if (hpos[0]-tpos[0])==-1:
                            tpos[0]=tpos[0]-1
                            tpos[1]=tpos[1]+1
                        elif (hpos[0]-tpos[0])==1:
                            tpos[0]=tpos[0]+1
                            tpos[1]=tpos[1]+1
                        else:
                            tpos[1]=tpos[1]+1
                        if tpos not in tgone:
                            tgone.append([tpos[0],tpos[1]])
                klist[0][1]=klist[0][1]+1
        elif line[0]=="D":
            for y in range(int(line[2:])):
                for x in range(1,len(klist)):
                    hpos=klist[x-1]
                    tpos=klist[x]
                    if (hpos[1]-tpos[1])==-1:
                        if (hpos[0]-tpos[0])==-1:
                            tpos[0]=tpos[0]-1
                            tpos[1]=tpos[1]-1
                        elif (hpos[0]-tpos[0])==1:
                            tpos[0]=tpos[0]+1
                            tpos[1]=tpos[1]-1
                        else:
                            tpos[1]=tpos[1]-1
                        if tpos not in tgone:
                            tgone.append([tpos[0],tpos[1]])
                klist[0][1]=klist[0][1]-1
        elif line[0]=="L":
            for y in range(int(line[2:])):
                for x in range(1,len(klist)):
                    hpos=klist[x-1]
                    tpos=klist[x]
                    if (hpos[0]-tpos[0])==-1:
                        if hpos[1]-tpos[1]==1:
                            tpos[0]=tpos[0]-1
                            tpos[1]=tpos[1]+1
                        elif (hpos[1]-tpos[1])==-1:
                            tpos[0]=tpos[0]-1
                            tpos[1]=tpos[1]-1
                        else:
                            tpos[0]=tpos[0]-1
                        if tpos not in tgone:
                            tgone.append([tpos[0],tpos[1]])
                klist[0][0]=klist[0][0]-1
        elif line[0]=="R":
            for y in range(int(line[2:])):
                for x in range(1,len(klist)):
                    hpos=klist[x-1]
                    tpos=klist[x]
                    if (hpos[0]-tpos[0])==1:
                        if hpos[1]-tpos[1]==1:
                            tpos[0]=tpos[0]+1
                            tpos[1]=tpos[1]+1
                        elif (hpos[1]-tpos[1])==-1:
                            tpos[0]=tpos[0]+1
                            tpos[1]=tpos[1]-1
                        else:
                            tpos[0]=tpos[0]+1
                        if tpos not in tgone:
                            tgone.append([tpos[0],tpos[1]])
                klist[0][0]=klist[0][0]+1
    print()
main()