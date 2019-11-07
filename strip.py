import sys
tracefile = open(sys.argv[1],'r+')
i = 1
for lines in tracefile:
    if i == 1:
        i+=1
    else:
        print(lines.rstrip("\n"))