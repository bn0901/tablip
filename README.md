# tablip
tablip can deal & generate multi-type of file.

tablip可以处理和生成多种类型文件。

### 功能列表

* Excel (Sets + Books) +auto column width!!!（智能调整列宽！！！）
* JSON (Sets + Books)
* YAML (Sets + Books)
* Pandas DataFrames (Sets)
* HTML (Sets)
* Jira (Sets)
* TSV (Sets)
* ODS (Sets)
* CSV (Sets)
* DBF (Sets)



### 特点

* 超简单使用
* 超强大功能
* 导出excel文件，也就是xls格式，自动优化列宽!!!!



### 安装

```cmd
pip install tablip
```

### 使用

```python
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
```

结果展示: []

### 关于

author:bn.zheng
contact with email: zhengbingxian666@163.com


