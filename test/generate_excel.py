# pip install tablip

import tablip

# 初始化表格 表名及表头
data = tablip.Dataset()
data.headers=['name','age']
data.title = 'test'

# 写入数据
content = [['lily','18'],
           ['lucy','20']]

for row in content:
    data.append(row)


# 导出excel
with open('test.xls','wb') as f:
    f.write(data.export('xls'))
