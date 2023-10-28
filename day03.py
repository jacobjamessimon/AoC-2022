def main():
    lines=[]
    total=0
    with open("C:\\Users\\Jacob\\AoC\\day03.txt") as f:
        lines=f.readlines()
    for x in range(0,len(lines),3):
        charac=check_strings(lines[x],lines[x+1],lines[x+2])
        total+=get_val(charac)
    print(total)
def get_val(charac):
    if charac.isupper():
        return (ord(charac)-38)
    else:
        return (ord(charac)-96)
def check_strings(str1,str2,str3):
    for a in str1:
        for b in str2:
            for c in str3:
                if a==b:
                    if b==c:
                        return a
main()
