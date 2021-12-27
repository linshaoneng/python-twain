# -*- coding: utf-8 -*-

# 林少能 linshaoneng@sina.cn
# 基于twain扫描仪程序
# Scanner program based on Twain

from libs import twain

# 扫描一张
# Scan one
try:
    twain.acquire(r'D:/scan/test.png', ds_name='SPK8021' ,
                  dpi=300, pixel_type="color")
except Exception as e:
    print(e)

exit()

# 连续扫描多张
# Continuous scanning of multiple sheets
try:
    twain.acquires(r'D:/scan/', '.png', ds_name='SPK8021',
                   dpi=300, pixel_type="color")
except Exception as e:
    # ConditionCode = 29 扫描仪没有纸/There is no paper in the scanner
    # ConditionCode = 24 扫描仪没有合好/扫描仪没有合好
    print(str(e) == "ConditionCode = 29")
