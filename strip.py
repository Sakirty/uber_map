import sys
#2019-10-06 15_00_00.csv
input_str = "./gps/2019-10-" +sys.argv[1]+" "+sys.argv[2]+"_00_00.csv"
#print(input_str)
#f = open("demofile2.txt", "a")
file_name = sys.argv[1]+sys.argv[2]+".txt"
file_f = open(file_name, "a")

tracefile = open(input_str,'r+')
i = 1
for lines in tracefile:
    if i == 1:
        i+=1
    else:
        file_f.write(lines.rstrip("\n"))
        file_f.write("\n")
file_f.close()
