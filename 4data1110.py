import sys
#2019-10-06 15_00_00.csv
input_str = './data1110/UberData.csv'
#print(input_str)
#f = open("demofile2.txt", "a")
file_f = open(input_str, 'r+')

i = 0
money = 0
distance = 0
duration = 0
for lines in file_f:
    if i == 0:
        i+=1
    else:
        distance += float(7)
        duration += float(8)
        money += float(11)
        i+=1
i = float(i)
print(str(distance))
print(str(duration))
print(str(money))
print(str(i))
avg_d = float(distance/i)
print(str(avg_d))
print(str(duration/i))
print(str(money/i))
