import re
stk=[]
def main():
    lines=[]
    with open("C:\\Users\\Jacob\\AoC\\day05.txt") as f:
        lines=f.readlines()
    for x in range(1,34,4):
        tmpstk=[]
        for y in range(0,8):
            if lines[y][x]!=' ':
                tmpstk.append(lines[y][x])
        stk.append(tmpstk)
    for x in range(10,len(lines)):
        act=re.findall('\d+',lines[x])
        perfact(act)
    for x in range(0,9):
        print(stk[x][0])
    
def perfact(act):
    mv=int(act[0])-1
    start=int(act[1])-1
    end=int(act[2])-1
    for x in range(mv,-1,-1):
        stk[end].insert(0,(stk[start].pop(x)))
main()
    