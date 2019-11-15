import os
'''
#2019-10-06 15_00_00.csv
input_str = "./gps/2019-10-" +sys.argv[1]+" "+sys.argv[2]+"_00_00.csv"
file_name = "./txts/"+sys.argv[1]+sys.argv[2]+".txt"
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

#tracefile = open(input_str,'r+')
for filename in os.listdir("./SG00110/gps"):
    if filename.endswith(".csv"): 
        print(os.path.join( filename))
        continue
'''
for filename in os.listdir("./SG00110/gps"):
    input_str = os.path.join("./SG00110/gps/"+filename)
    file_name = "./ALL_DATA.txt"
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
    