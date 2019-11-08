# uber
usages:
for strip.py:
用来提取csv的数据的，在terminal里这样使用：
    - 将GPS文件夹放在与该文件统一文件夹下
    - python3 strip.py [ 日期 ] [ 时间 ]
        - 命令行注意空格， 不然会报错
    - 输出文件会保存在./txts中，请确保先建立该文件夹，不然会报错

for print.py
    - 使用之前先pip install gmplot
        - python3: pip3 install gmplot
    - 执行：
        - python3 print.py [ 文件名字 ]
            - [ 文件名字 ]是从./txts中提取已有的txt文件来做，不需要加.txt后缀
            - 生成的地图会自动保存在./GPSMAP中，请确保先建立该文件夹，不然会报错
