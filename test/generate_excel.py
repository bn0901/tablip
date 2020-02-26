# pip install tablip

import tablip

# 初始化表格 表名及表头
data = tablip.Dataset()
data.headers=['姓名','年龄','地址']
data.title = '个人信息'

# 写入数据
content = [['小明','18','Stanford University'],
           ['小王','20','Stanford University 450 Jane Stanford Way Stanford, CA 94305–2004']]

for row in content:
    data.append(row)

# 导出excel
with open('test.xls','wb') as f:
    f.write(data.export('xls'))
