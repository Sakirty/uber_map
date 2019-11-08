# uber
usages:<br>
for strip.py:<br>
用来提取csv的数据的，在terminal里这样使用：<br>
    - 将GPS文件夹放在与该文件统一文件夹下<br>
    - python3 strip.py [ 日期 ] [ 时间 ]<br>
        - example: 2019-10-06 15_00_00.csv<br>
            - python3 strip.py 06 15<br>
            - 这样就行了,会生成0615.txt<br>
        - 命令行注意空格， 不然会报错<br>
    - 输出文件会保存在./txts中，请确保先建立该文件夹，不然会报错<br>

for print.py<br>
    - 使用之前先pip install gmplot<br>
        - python3: pip3 install gmplot<br>
    - 执行：<br>
        - python3 print.py [ 文件名字 ]<br>
            - [ 文件名字 ]是从./txts中提取已有的txt文件来做，不需要加.txt后缀<br>
                - python3 print.py 0615<br>
                - 会生成100615.html，就是地图文件<br>
            - 生成的地图会自动保存在./GPSMAP中，请确保先建立该文件夹，不然会报错<br>
