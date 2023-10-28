from anytree import Node, RenderTree
base=Node("/")
prevdir=""
currdir=""
def main():
    lines=[]
    with open("C:\\Users\\Jacob\\AoC\\day07.txt") as f:
        lines=f.readlines()
    for line in lines:
        line=line.strip()
        if line[2:4]=="cd":
            isLS=False
            cd(line[5:])
        elif isLS:
            if line[0].isdigit():
                print("File: "+line)
            elif line[0:2]=="dir":
                print("Dir is: "+line[3:])
        elif line[2:4]=="ls":
            isLS=True

def cd(str):
    if str=="..":
        currdir=prevdir
    else:
        prevdir=currdir
        currdir=str
main()