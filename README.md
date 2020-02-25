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
```

### 关于
author:bn.zheng
contact with email: zhengbingxian666@163.com


