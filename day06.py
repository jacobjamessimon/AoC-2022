def main():
    lines=[]
    with open("C:\\Users\\Jacob\\AoC\\day06.txt") as f:
        lines=f.readlines()
    line=lines[0]
    for x in range(14,len(line)):
        if len(set(line[x-14:x]))==14:
            print(x)
            break
main()