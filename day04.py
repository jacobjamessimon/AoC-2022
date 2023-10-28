def main():
    lines=[]
    total=0
    with open("C:\\Users\\Jacob\\AoC\\day04.txt") as f:
        lines=f.readlines()
    for line in lines:
        splitline=line.split(",")
        total+=checkrange(splitline[0], splitline[1])
    print(total)

def checkrange(str1,str2):
    rng1=str1.split("-")
    rng2=str2.split("-")

    rng1min=int(rng1[0])
    rng1max=int(rng1[1])
    
    rng2min=int(rng2[0])
    rng2max=int(rng2[1])

    if len(range(max(rng1min,rng2min),min(rng1max,rng2max)+1))!=0:
        return 1
    else:
        return 0
main()